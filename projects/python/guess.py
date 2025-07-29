""" Welcome to the guess game!!!
    The game goes like this:
    1-you should specify a number for the balls
    Game Rules:
    1-You'll be asked about the color for each ball you specified
    2-If your (green balls > red balls), You win
    3-If your (red balls > green balls), You lose
"""
import random

bls = int(input("Enter a number for the balls: "))

clrs = ["Green", "Red"]

match = 0
mis_match = 0
x = 0

while (x < bls):

    usr_clr_choice = input("What is your choice? ")

    if (usr_clr_choice != ("Green" or "Red")):
        print("Hey! Enter a valid color.")
        continue

    rand_clr_choice = clrs[random.randint(0, len(clrs) - 1)]


    if (usr_clr_choice == rand_clr_choice):
        match += 1

    else:
        mis_match += 1
    print(f"Your score is: {match}")
    
    x += 1

if (match > mis_match):
    print("Nice, You won.")
else:
    print("Oh no, You lost!")
