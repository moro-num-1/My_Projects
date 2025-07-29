#Data
developer = True
age = -1
html = False
css = False
js = False
python = True
php = True
lara = True

#If statements
if (developer == True and 10 > age > 0):
    print("You must scratch Now!!!")

elif (developer == True and 16 > age > 10):
    print("You should print('Hello, World')")

elif (developer == True and 20 > age > 16):
    if (html and css and js):
        print("You're a front-end developer")
    elif (python and php and lara):
        print("You're a back-end developer")
    else:
        print("Hey! Choose anything.")

elif(developer == True and age > 20):
    print("Don't do anything. It'll be on Robots after few days.")

elif (not developer):
    print("You can be a graphic designer. or anything else u like.")

elif (0 >= age):
    print("Are u kidding me?, You must be born first.")

else:
    print("There is an error.")