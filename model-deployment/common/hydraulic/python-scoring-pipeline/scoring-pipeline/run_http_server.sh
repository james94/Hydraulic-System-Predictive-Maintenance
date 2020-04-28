#!/usr/bin/env bash

set -o pipefail
set -ex

# pip is default package manager
pm=pip

current_dir="$(pwd)"
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

run_using_pip(){
    if [ ! -d http_server_env ]; then
        echo "Creating virtual environment..."
        if [ "${SCORING_PIPELINE_INSTALL_DEPENDENCIES}" == "0" ]; then
            virtualenv -p python3.6 --system-site-packages http_server_env
            http_server_env/bin/python -m pip install scoring_*.whl
        else
            virtualenv -p python3.6 http_server_env
            source http_server_env/bin/activate

            python -m pip install --upgrade --upgrade-strategy only-if-needed pip==19.3.1

            echo "Installing dependencies..."
            pip install --upgrade --upgrade-strategy only-if-needed -r requirements.txt

            echo "Installing server dependencies..."
            pip install --upgrade --upgrade-strategy only-if-needed -r http_server_requirements.txt

            deactivate
        fi
    fi

    source http_server_env/bin/activate
    python http_server.py --port=9090
    deactivate
}

run_using_conda(){
    env_name="$(head -n 1 environment.yml | cut -d ' ' -f 2)"
    create_conda_env ${env_name}
    source activate ${env_name}
    python http_server.py --port=9090
    source deactivate
}

cd "${script_dir}"
source "./common-functions.sh"

main $@
cd "${current_dir}"
