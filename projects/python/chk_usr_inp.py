username = input("What is your name? ")

if (len(username) > 12):
    print("The name mustn't contain more than 12 character!")
elif (username.count(" ") != 0):
    print("The name mustn't contain any space!")
elif (username.isalpha() == False):
    print("Digits aren't allowed!")
else:
    print(f"Welcome {username}!")