#!/usr/bin/bash

x=1

while [[ x -le 10 ]]
do
    read -p "Pushup $x: press enter to continue"
    echo "Hey, I just did $x pushups"
    ((x ++))
done
echo "Congrats, you completed your pushups!!"
