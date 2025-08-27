import random as rand
low_num = 1
hei_num = 100
rand_num = rand.randint(low_num, hei_num)
num_of_gus = 0
is_running = True
while is_running:
    gus_num = input("Enter your guess: ")
    if not gus_num.isdigit():
        print(f"{gus_num} is not a number, Enter a number between {low_num} and {hei_num}.")
    else:
        gus_num = int(gus_num)
        num_of_gus += 1
        if (gus_num > hei_num or gus_num < low_num):
            print(f"{gus_num} is out of range. Enter a number between {low_num} and {hei_num}")
        elif (rand_num < gus_num):
            print("Too high! Try again!")
        elif (rand_num > gus_num):
            print("Too low! Try again!")
        else:
            print(f"Correct! The answer was {rand_num}")
            print(f"Number of guesses: {num_of_gus}")
            is_running = False