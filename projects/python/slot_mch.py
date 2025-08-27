import random
def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row [0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    else:
        return 0

def main():
    print("*************************")
    print("Welcome to Python slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    balance = 100

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Place your bet amount: ")
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient bunds!!")
            continue
        if bet <= 0:
            print("Bet must be greater than 0")
            continue
        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry, you lost this round")
        balance += payout
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != "Y":
            break
    print("********************************************")
    print(f"Game Over! Your final balance is ${balance}")
    print("********************************************")




if __name__ == "__main__":
    main()