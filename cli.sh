source ./inc/sh/functions.sh

if [[ "$1" == "help" ]]; then
    echo "-= HELP =-"
    echo "help    >> Gives help for this cli"
    echo "remlogs >> Removes all the logs"
    echo "----------"

elif [[ "$1" == "remlogs" ]]; then
    if [[ "$2" != "" ]]; then
        rm -rf ./.private/$2

        exit
    fi

    printf "[ * ] Removing ./.private/logs " ; rm -rf ./.private/logs ; echo "[ OK ]"

    createLogs

else
    echo "Unknown command \`$1\`, type 'help' for more info"
fi


