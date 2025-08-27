import random as rand
#● ┌ ─ ┐ │ └ ┘
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│       ● │",
        "│         │",
        "│ ●       │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│       ● │",
        "│    ●    │",
        "│ ●       │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))
for die in range(num_of_dice):
    dice.append(rand.randint(1, 6))

x = 0
for line in range(5):
    for die in dice:
        print(dice_art[die][line], end = " ")
    print()
    x += 1

for die in dice:
    total += die
print(f"The total is {total}")