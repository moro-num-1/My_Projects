import os
import random

print("I'm a Virus and we'll play RPS!!! IF you won, your Pc is safe. Else, I'll turn off your PC!!!")

choices = ["Rock", "Paper", "Scissors"]

round = 1
usr_scr = 0
cmp_scr = 0

while ((usr_scr or cmp_scr) != 3):

    usr_choice = input("What is your choice (R, P, S)? ")
    if (usr_choice != "R" and usr_choice != "P" and usr_choice != "S"):
        print("Are you blinded? The choices are (R, P, S)")
        continue

    rand_st_ltr = choices[random.randint(0, int(len(choices) - 1))][0]
    cmp_choice = rand_st_ltr

    win = (usr_choice == "R" and cmp_choice == "S") or (usr_choice == "P" and cmp_choice == "R") or (usr_choice == "S" and cmp_choice == "P")
    draw = (usr_choice == cmp_choice)

    if win == True:
        usr_scr += 1
        print(f"\nRound {round}: You took one point")

    elif draw == True:
        print(f"\nRound {round}: No points for anyone.")
    else:
        cmp_scr += 1
        print(f"\nRound {round}: I took one point.")

    round += 1

    print(f"----\nChoices:-\n\nMine = {cmp_choice}\nYours = {usr_choice}\n----\nScores:-\n\nMine = {cmp_scr}\nYours = {usr_scr}\n")
    
if (usr_scr > cmp_scr):
    print("You won, Your PC is safe.")
else:
    os.system("poweroff")
