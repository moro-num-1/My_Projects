import os
accounts = [["example@gmail.com", "example", "example1234"]]
print("Choices:-\n-------\n1-Register if you want to make a new account.\n2-Login if you want to log in.\n3-See if you want to see the current emails and usernames.\n4-Clear if you want to clear the screen.\n5-Quit if you want to exit.")
while True:
    #take a choice
    choice = input("\nLogin or Register or See(L, R, S), (Q to quit) (C to clear screen): ")
    #if the user want to register;
    if choice.lower() in ["r", "register"]:
        #make a new email;
        new_email = input("\nEnter an email address (example@gamil.com): ")
        while (not new_email.endswith("@gmail.com")):
            new_email = input("\nEnter a valid email (example@gmail.com): ")
        #check if the acount is created before;
        x = 0
        while (x < len(accounts)):
            email = accounts[x][0]

            if email == new_email:
                new_email = input("\nSorry, This email is taken, Try another one: ")
                while (not new_email.endswith("@gmail.com")):
                    new_email = input("\nEnter a valid email (example@gmail.com): ")
                x = 0
                continue
            x += 1
        #if the account is NOT created before;
        usr_name = input("\nEnter a user name: ")
        while (len(usr_name) > 12):
            usr_name = input("\nThe user name mustn't contain more than 12#, try again: ")
        psw = input("\nCreate a password for your email: ")
        print("\nRegistered successfully!")
        accounts.append([new_email, psw, usr_name])
    #elif the user want to login;
    elif choice.lower() in ["l", "login"]:
        #take the user email;
        log_email = input("\nEnter your email: ")
        while (not log_email.endswith("@gmail.com")):
            log_email = input("\nEnter a valid email address (example@gmail.com): ")
        #check if the account does exist;
        x = 0
        while (x < len(accounts)):
            email = accounts[x][0]
            psw = accounts[x][1]
            usr_name = accounts[x][2]
            if (log_email != email):
                x += 1
                continue
            #if the email exists;
            else:
                usr_psw = input("\nWhat is the password? ")
                if (usr_psw == psw):
                    print("\nLogged in successfully!")
                    print(f"\nWelcome, {usr_name}.")
                else:
                    print("\nThe password isn't correct, try to login again.")
                break
        #if the loop reached the end and didn't find the user email
        if (x == len(accounts)):
            print("\nThis email doesn't exist, try again.")
    #elif the user want to see the emails;
    elif (choice.lower() in ["s", "see"]):
        emails = []
        for account in accounts:
            email = account[0]
            usr_name = account[2]
            emails.append([f"{email} : {usr_name}"])
        print(f"\n{emails}")
    #elif the user want to clear the screen;
    elif (choice.lower() in ["c", "clear"]):
        os_name = os.name
        if (os_name == "posix"):
            os.system("clear")
        elif (os_name == "nt"):
            os.system("cls")
        else:
            print("Sorry, I've not managed this on your OS.")
    #elif the user want to exit;
    elif choice.lower() in ["q", "quit"]:
        break
    #if the user choose invalid choice;
    else:
        print(f"\n{choice} is NOT a valid choice!!")