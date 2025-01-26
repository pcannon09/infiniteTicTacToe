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
printf "[ * ] Creating \`.private/logs\` "; mkdir ./.private/logs ; echo "[ OK ]"
printf "[ * ] Creating \`.private/logs/main-logs.txt\` "; touch ./.private/logs/main-logs.txt ; echo "[ OK ]"
printf "[ * ] Creating \`.private/data\` "; mkdir ./.private/data ; echo "[ OK ]"

