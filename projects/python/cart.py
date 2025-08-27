menu = {
    "pizza" : 3.00,
    "nachos" : 4.50,
    "popcorn" : 6.00,
    "fries" : 2.50,
    "chips" : 1.00,
    "pretzel" : 3.50,
    "soda" : 3.00,
    "lemonade" : 4.25
}
print("------------- Menu -------------\n")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("\n--------------------------------")

total = 0
items = []

while (True):
    choice = input("\nDo you want to buy or remove an item (y / n)? ")
    if choice.lower() == "y":
        item = input("\nWhat is the item? ").lower()
        if not item in menu:
            print("\nI don't have this item, try again.")
            continue
        decision = input("\nBuy or Remove (B, R)? ").lower()
        if decision == "b":
            items.append(item)
            total += menu[item]
        elif decision == "r":
            if item in items:
                items.remove(item)
                total -= menu[item]
            else:
                print("\nThis item isn't in your cart, try again.")
    elif choice.lower() == "n":
        break
    else:
        print("\nEnter a valid choice!")
        continue
    print(f"Your items are {items}")

if total != 0:
    print(f"\nYour items cost ${total:.2f}")