#Declaring variables;
#Declaring Functions
balance = 0
def show_balance():
    print(f"Your balance is ${balance:.2f}")
def deposit():
    global balance
    dep_amount = float(input("Enter an amount to be deposited: "))
    if dep_amount < 0:
        print(f"{dep_amount} is NOT a valid number, Try again!!")
    else:
        balance += dep_amount
def withdraw():
    global balance
    if balance == 0:
        print("You've NOT any balance to withdraw from!!")
    else:
        wdr_amount = float(input("Enter an amount to be withdrawn: "))
        if wdr_amount > balance:
            print("This number is above your amount!! Try again")
        else:
            balance -= wdr_amount
def display_options():
    print("************* Banking Programme *************")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

#Coding
def main():
    banking = True
    while banking:
        #Display options;
        display_options()
        choice = int(input("Enter your choice (1-4): "))
        
    #Processing the choice;
        
        #If the user wants to show his balance;
        if choice == 1:
            show_balance()

        #Else if the user wants to deposit;
        elif choice == 2:
            deposit()

        #Else if the user wants to withdraw
        elif choice == 3:
            withdraw()

        #Elif the user wants to exit;
        elif choice == 4:
            banking = False

        #Elif the user entered an invalid option;
        else:
            print(f"{choice} is an invalid option!! Try again")
    print("Thank you, Have a Nice day!!")

if __name__ == "__main__":
    main()