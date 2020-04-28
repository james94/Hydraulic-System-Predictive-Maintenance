error_exit() {
    echo "$1" 1>&2 
    exit 1
}

print_usage(){
    echo "Usage:"
    echo "  bash $0 [-h | --help] [--pm <package manager>]"
    echo "Options:"
    echo "  -h, --help                  Display usage information."
    echo "  --pm <package manager>      Package manager to use. Options are either 'pip' or 'conda'."
}

parse_args_and_exec(){
    while [ "$1" != "" ]; do
        case "$1" in
            --pm )
                shift
                pm="$1"
                if [[ -z "${pm}" || ("${pm}" != "pip" && "${pm}" != "conda") ]]; then
                    print_usage
                    error_exit "Error: Incorrect parameters passed"
                fi
                ;;
            -h | --help )
                print_usage
                exit 0
                ;;
            * )
                print_usage
                error_exit "Error: Incorrect parameters passed"
                ;;
            esac
            shift
    done

    if [[ "${pm}" == "pip" ]]; then
        run_using_pip
    fi

    if [[ "${pm}" == "conda" ]]; then
        run_using_conda
    fi
}

create_conda_env(){
    env_name=$1
    env_created="$(conda env list | grep ${env_name} | wc -l)"
    if [[ "${env_created}" == 0 ]]; then
        echo "Creating conda environment ${env_name}"
        if ! conda env create -f environment.yml; then
            echo "Retrying after adjusting failed conda dependencies"
            # move failed conda dependencies to be handled by pip
            conda env create -f environment.yml 2>&1 >/dev/null | grep "==" > condafaildeps.txt
            grep -Fvx -f condafaildeps.txt environment.yml > environment.yml.tmp
            mv environment.yml.tmp environment.yml
            cat condafaildeps.txt | sed 's/^/    /' >> environment.yml
            
            # retry creating environment
            conda env create -f environment.yml
        fi
    fi
}

main(){
    parse_args_and_exec $@
}