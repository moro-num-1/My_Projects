emails = [["example@gmail.com", "example"]]
while True:
    #take a choice
    choice = input("Login or Register (L, R), (q to quit): ")
    #if the choice was Register;
    if choice.lower() == "r":
        #make a new email;
        new_email = input("Enter an email address (example@gamil.com): ")
        while (not new_email.endswith("@gmail.com")):
            new_email = input("Enter a valid email (example@gmail.com): ")
        #check if the acount is created before;
        x = 0
        while (x < len(emails)):
            email = emails[x][0]

            if email == new_email:
                new_email = input("Sorry, This email is taken, Try another one: ")
                while (not new_email.endswith("@gmail.com")):
                    new_email = input("Enter a valid email (example@gmail.com): ")
                x = 0
                continue
            x += 1
        psw = input("Create a password for your email: ")
        emails.append([new_email, psw])
    #elif the choice was Login;
    elif choice.lower() == "l":
        #check if the account does exist;
        log_email = input("Enter your email: ")
        x = 0
        while (x < len(emails)):
            if (log_email != emails[x][0]):
                x += 1
                continue
            #if the email exists;
            else:
                usr_psw = input("What is the password? ")
                if (usr_psw == emails[x][1]):
                    print(f"Welcome, {log_email}")
                else:
                    print("The password isn't correct, try to login again.")
                break
        #if the loop reached the end and didn't find the user email
        if (x == len(emails)):
            print("This email doesn't exist, try again.")
            
    #elif the user want to exit;
    elif choice.lower() == "q":
        break
    #if the user choose invalid choice;
    else:
        print(f"{choice} is NOT a valid choice.")