print()
print()
print()
print("                                                                    Welcome to Moro's calculator                                       ")
print("                                                                    ----------------------------                                       ")

#Define the Mark

mark = input("Enter the mark: ")

#test the mark before continue

if mark not in ["+", "-", "*", "/"]:
	print("This mark is invalid!!!")
	print()
	quit()

#Define the numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#If conditions

if mark == "+":
	result = num1 + num2
elif mark == "-":
	result = num1 - num2
elif mark == "*":
	result = num1 * num2
elif mark == "/":
	if num2 != 0:
		result = num1 / num2
	else:
		print("Numbers can't divide by zero!!!")
print(result)