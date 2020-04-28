#!/usr/bin/env bash

set -o pipefail
set -ex

# pip is default package manager
pm=pip

current_dir="$(pwd)"
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

run_using_pip(){
    if [ ! -d env ]; then
        echo "Creating virtual environment..."
        if [ "${SCORING_PIPELINE_INSTALL_DEPENDENCIES}" == "0" ]; then
            virtualenv -p python3.6 --system-site-packages env
            env/bin/python -m pip install --upgrade --upgrade-strategy only-if-needed scoring_h2oai_experiment*.whl
        else
            virtualenv -p python3.6 env
            source env/bin/activate

            python -m pip install --upgrade --upgrade-strategy only-if-needed pip==19.3.1 pkginfo==1.5.0.1
            rm -rf requirements_full.txt
            for fil in `cat requirements.txt`
            do
                if [[ "$fil" == *".whl"* ]]
                then
                    echo "IN:"$fil
                    pkginfo --csv --single -f 'requires_dist' $fil |tr , '\n'|sed 's/ (//g'|sed 's/)//g' >> requirements_full.txt
                else
                    echo "OUT:"$fil
                fi
                                           
            done
            grep -v pandas-ml requirements_full.txt > requirements_full.txt.tmp
            mv requirements_full.txt.tmp requirements_full.txt

            echo "Installing dependencies..."
            python -m pip install --upgrade --upgrade-strategy only-if-needed -r requirements.txt -c requirements_full.txt

            deactivate
        fi

        source env/bin/activate
        echo "---- Install CPU and GPU tensorflow ----"
        # for clean install and real testing of dynamic loading, need base tensorflow to not be there
        pip uninstall -y tensorflow
        pip uninstall -y tensorflow-gpu
        pip install tensorflow==1.13.1 --upgrade --upgrade-strategy only-if-needed
        tf_path=`python -c "import os ; import importlib.util ; tf_loader = importlib.util.find_spec('tensorflow') ; print(os.path.dirname(tf_loader.origin))"` ; \
        cpu_ext="_cpu" ; \
        tf_path_cpu=$tf_path$cpu_ext ; \
        echo $tf_path ; \
        echo $cpu_ext ; \
        echo $tf_path_cpu ; \
        rm -rf $tf_path_cpu ; \
        mv $tf_path $tf_path_cpu ; \
        pip install tensorflow-gpu==1.13.1 --upgrade --upgrade-strategy only-if-needed ; \
        gpu_ext="_gpu" ; \
        tf_path_gpu=$tf_path$gpu_ext ; \
        echo $tf_path ; \
        echo $gpu_ext ; \
        echo $tf_path_gpu ; \
        rm -rf $tf_path_gpu ; \
        mv $tf_path $tf_path_gpu
        deactivate

    fi

    source env/bin/activate
    python example.py
    deactivate
}

run_using_conda(){
    env_name="$(head -n 1 environment.yml | cut -d ' ' -f 2)"
    create_conda_env ${env_name}
    source activate ${env_name}
    python example.py
    source deactivate
}

cd "${script_dir}"
source "./common-functions.sh"

main $@
cd "${current_dir}"
