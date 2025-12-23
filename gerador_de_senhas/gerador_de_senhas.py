import random

def menu():
    print("======================================")
    print("<><><><>==PASSWORD GENERATOR==<><><><>")
    print("======================================")
    print("[1] Lowercase (a-z)")
    print("[2] Uppercase (A-Z)")
    print("[3] Numbers (0-9)")
    print("[4] Simbols (!@#$%&)")
    print("======================================")
    print('!Answer the questions!')
    print("======================================")


def get_user_choice():
    lowercases = "abcdefghijklmnopqrstuvwxyz"
    uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    simbols = "!@#$%&*/"
    all_characters = ""

    length = int(input("What the length of your password: "))
    collection1 = str(input("Do you want [1]Lowercase - [Y/N]: ")).upper()
    collection2 = str(input("Do you want [2]Uppercase - [Y/N]: ")).upper()
    collection3 = str(input("Do you want [3]Numbers - [Y/N]: ")).upper() 
    collection4 = str(input("Do you want [4]Simbols - [Y/N]: ")).upper()

    print("======================================")
    print("!OK let's Generate a password for you!")
    print("======================================")
    
    if collection1 == "Y":
        all_characters += lowercases
    if collection2 == "Y":
        all_characters += uppercases
    if collection3 == "Y":
        all_characters += numbers
    if collection4 == "Y":
        all_characters += simbols

    if collection1 =="N" and collection2 =="N" and collection3 =="N" and collection4 == "N":
        print("===OPS! You need to select some option to generate a password.===")  

    return all_characters, length

def password_generator(all_characters, length):
    password = ""
    if not all_characters:
        return

    for reptition in range(length):
       password += random.choice(all_characters)

    print(f"Your Passwaord is {password}")

menu()
allcharacter, passwordlength = get_user_choice()
password_generator(allcharacter,passwordlength)