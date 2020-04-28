#!/usr/bin/env bash

set -o pipefail
set -ex

# pip is default package manager
pm=pip

current_dir="$(pwd)"
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

run_using_pip(){
    if [ ! -d tcp_client_env ]; then
        echo "Creating virtual environment..."
        if [ "${SCORING_PIPELINE_INSTALL_DEPENDENCIES}" == "0" ]; then
            virtualenv -p python3.6 --system-site-packages tcp_client_env
            tcp_client_env/bin/python -m pip install scoring_*.whl
        else
            virtualenv -p python3.6 tcp_client_env
            source tcp_client_env/bin/activate

            echo "Installing client dependencies..."
            pip install -r client_requirements.txt

            deactivate
        fi

        echo "Compiling Thrift client..."
        thrift --gen py scoring.thrift

        echo "Postprocessing Thrift..."
        source tcp_client_env/bin/activate
        python thrift_post_processing.py
        deactivate
        mv temp_ttypes.py gen-py/h2oai_scoring/ttypes.py
    fi

    source tcp_client_env/bin/activate
    python example_client.py
    deactivate
}

run_using_conda(){
    env_name="$(head -n 1 environment.yml | cut -d ' ' -f 2)"
    create_conda_env ${env_name}

    echo "Compiling Thrift server..."
    thrift --gen py scoring.thrift

    echo "Postprocessing Thrift..."
    source activate ${env_name}
    python thrift_post_processing.py
    mv temp_ttypes.py gen-py/h2oai_scoring/ttypes.py
    python example_client.py
    source deactivate
}

cd "${script_dir}"
source "./common-functions.sh"

main $@
cd "${current_dir}"
