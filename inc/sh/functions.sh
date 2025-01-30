function createLogs(){
    printf "[ * ] Creating \`.private/logs\` "; mkdir ./.private/logs ; echo "[ OK ]"
    printf "[ * ] Creating \`.private/logs/game-sys-logs.txt\` "; touch ./.private/logs/main-logs.txt ; echo "[ OK ]"
    printf "[ * ] Creating \`.private/logs/main-logs.txt\` "; touch ./.private/logs/main-logs.txt ; echo "[ OK ]"
}

function createData(){
    printf "[ * ] Creating \`.private/data\` "; mkdir ./.private/data ; echo "[ OK ]"
}

