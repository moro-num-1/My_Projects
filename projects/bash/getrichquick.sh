#!/usr/bin/bash

echo "What is your name?"
read name
echo "How old are you?"
read age

echo "Hello, $name, you are $age old."

getrichat=$((($RANDOM%14)+$age))

echo "You will get rich at $getrichat"
