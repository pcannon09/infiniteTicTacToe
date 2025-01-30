source ./inc/sh/functions.sh

echo "[ * ] Generating files"

if [[ "$1" == "--ungen" ]]; then
    echo "[ WARN ] ARE YOU SURE THAT YOU WANT TO DELETE THE FOLLOWING DIRECTORIES?"
    echo "[  *   ] .private"
    echo "[  *   ] Press return to continue. Press CTRL + C to cancel"

    read

    printf "[ * ] Deleting \`.private\` " ; rm -rf ./.private/ ; echo "[ OK ]"

    exit
fi

printf "[ * ] Creating \`.private/\` "; mkdir ./.private ; echo "[ OK ]"

createLogs ; createData

