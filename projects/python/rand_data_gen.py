#        ---------------Data-Generator---------------;

#Importing modules;
import random as rand, string

#Declaring global variables;
email_chars = string.ascii_lowercase
domains = ["gmail", "yahoo", "outlook", "icloud"]
tlds = [".com", ".net", ".org", ".edu", ".us", ".uk", ".ru", ".de", ".info", ".nl", ".gov"]
username_chars = "_" + "." + string.digits + string.ascii_lowercase
psw_chars = string.ascii_letters + string.punctuation + string.digits
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#Generate a random email;
def gen_rand_email():
    tld = rand.choice(tlds)
    domain = rand.choice(domains)
    email_username_list = []
    for counter in range(rand.randint(5, 13)):
        email_username_list.append(rand.choice(email_chars))
    email_username = "".join(email_username_list)
    email = email_username + "@" + domain + tld
    return email

#Generate a random username;
def gen_rand_username():
    username_list = []
    for counter in range(rand.randint(4, 14)):
        username_list.append(rand.choice(username_chars))
    username = "".join(username_list)
    return username

#Generate a random password;
def gen_rand_psw():
    psw_list = []
    for counter in range(rand.randint(8, 20)):
        psw_list.append(rand.choice(psw_chars))
    psw = "".join(psw_list)
    return psw

#Generate a random birthday;
def gen_rand_birth():
    
    birth = f"{rand.choice(months)}/{rand.randint(1, 30)}/{rand.randint(1880, 2012)}"
    return birth

#Title;
print("-------------Welcome to Discord Data Generator-------------\n")

#Process the input;
fields_num = input("How many email do you want to generate? ")

if not fields_num.isdigit():
    print("Only numbers are allowed")

else:
    fields_num = int(fields_num)
    #Code section;
    for counter in range(fields_num):
        email = gen_rand_email()
        username = gen_rand_username()
        birth = gen_rand_birth()
        psw = gen_rand_psw()

        field = f"{counter+1}- [{email}; {username}; {psw}; {birth}]"
        print(field, end="\n\n")