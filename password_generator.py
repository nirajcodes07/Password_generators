# PASSWORD GENERATOR

import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%&*-_"

all_chars = lowercase + uppercase + numbers + symbols

while True:
    print("\nType 1 for new password : ")
    print("Type 2 for exit : ")
    
    choice = input("\nChoice : ")
    
    if choice == "1":
        length = int(input("KITNE CHARACTER KA PASSWORD CHAHIYE?  "))

        password = ""

        for i in range(length):
           character = random.choice(all_chars)
           password = password + character
    
        print("your password :", password)

    elif choice == "2":
        print("Thank you")
        break
    
    else:
        print("Only type 1 or 2")