#Take the user options;
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the last number: "))
sign = input("Enter the sign: ")
result = 0

#expect the possibilities.
if (sign == "+"):
    result = num1 + num2
elif sign == "-":
    result = num1 - num2
elif sign == "*":
    result = num1 * num2
elif sign == "/":
    result = num1 / num2
else:
    print("Enter a correct sign!!!")

#Print the final result to the console.
print(f"{num1} {sign} {num2} = {result}")