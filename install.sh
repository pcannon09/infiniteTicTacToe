source ./inc/sh/colors.sh

libs=(
    "pygame"
    "colorama"
    "typing"
)

libsDef=(
    "A library to create GUI-based games" 
    "Library that outputs colored text on the terminal output"
    "Declare constant variables in python and other things"
)

if [[ ! -d "pip_modules" ]]; then
    echo "[ * ] Creating \`pip_modules/\`"

    mkdir pip_modules/

    echo "[ OK ]"
fi

if [[ "$1" == "dev" ]]; then
    libs+=("pyinstaller")
    libsDef+=("Compile python program with pyinstaller")

elif [[ "$1" == "install" ]]; then
    if [[ "$2" == "" ]]; then
        echo "[ * ] Please pass the package name to install in the second param"

        exit
    fi

    echo "[ * ] Installing \`$2\`" ; pip3 install --target=./pip_modules $2 ; echo "[ OK ]"

    exit

elif [[ "$1" == "help" ]]; then
    echo -e "[ COMMANDS ]$BOLD"
    echo -e "help     > Show this help"
    echo -e "install  > Install a specific lib"
    echo -e "list     > Show the list of used libs for this project"
    echo -e "$RESET[ DONE ]"
    exit

elif [[ "$1" == "list" ]]; then
    echo "[ * ] Python dependencies"

    for libsIt in "${libs[@]}"; do
        LIBS=$libsIt
        for libsDefIt in "${libsDef[@]}"; do
            LIBSDEF=$libsDefIt
        done

        echo -e "LIB:$BOLD $LIBS |$DIM $LIBSDEF $RESET"
    done

    exit    

fi

for x in "${libs[@]}"; do
    echo "[ * ] Installing \`$x\`" ; pip3 install $x --break-system-packages ; echo "[ OK ]"
done

echo "[ DONE ]"

