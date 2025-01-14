if [[ ! -d "pip_modules" ]]; then
    echo "[ * ] Creating \`pip_modules/\`"
    mkdir pip_modules/
    echo "[ OK ]"
fi

echo "[ * ] Installing \`pygame\`" ; pip3 install --target=./pip_modules pygame ; echo "[ OK ]"
echo "[ * ] Installing \`colorama\`" ; pip3 install --target=./pip_modules colorama ; echo "[ OK ]"

echo "[ DONE ]"

