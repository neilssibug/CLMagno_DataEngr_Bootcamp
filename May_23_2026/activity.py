#print("Hello World!")
import time
from datetime import datetime

choice = ""

while choice != "X" :
    print("Hello World!")
    print("\nMenu:")

    print("[A] Variables")
    print("[B] Type cast & Transform")
    print("[C] Math operations")
    print("[D] Logical operations")
    print("[E] Validation")
    print("[F] Looping")
    print("[X] Exit")


    time.sleep(1)
    choice = input("\nChoose: ").upper()

    if choice == "A":
        in_choice = "n"
        
        while in_choice != "y":
            print("Variables:\n")
            is_string = "Welcome to Variables"
            is_integer = 10
            is_float = 1.5596
            is_boolean = True

            print(f"This is a {type(is_string)} : {is_string}")
            print(f"This is a {type(is_integer)} : {is_integer}")
            print(f"This is a {type(is_float)} : {is_float:,.2f}")
            print(f"This is a {type(is_boolean)} : {is_boolean}")

            """
            cust_name = "Ana Santos"
            cust_id = 1001
            balance = 2540.75731
            is_active = True

            print(f"Customer: {cust_name}")
            print(f"Customer ID: {cust_id}")
            print(f"Balance: {balance}")
            print(f"Active: {is_active}")
            print(f"{cust_name} has ₱{balance:,.2f}")
            """

            in_choice = input("\nBack: (y/n): ").lower()

    elif choice == "B":
        in_choice = "n"
        
        while in_choice != "y":
            print("Type cast & Transform:\n")

            first = input("Input your First Name: ").title()
            last = input("Input your Last Name: ").title()
            age = int(input("What is your Age: "))

            full_name = f"{first.strip()} {last.strip()}"
            print(f"{full_name} you're {age} y/o now!")

            in_choice = input("\nBack: (y/n): ").lower()

    elif choice == "C":
        in_choice = "n"
        
        while in_choice != "y":
            print("Math operations:\n")

            birth_year = int(input("What is your birth year: "))
            age_now = datetime.now().year - birth_year

            print(f"You are {age_now} y/o")

            in_choice = input("\nBack: (y/n): ").lower()

    elif choice == "D":
        in_choice = "n"
        
        while in_choice != "y":
            print("Logical operations:\n")

            mom_year = int(input("What is Mom's birth year: "))
            you_year = int(input("What is your birth year: "))

            mom_age = datetime.now().year - mom_year
            your_age = datetime.now().year - you_year

            if mom_age >= your_age:
                print(f"Your definitely younger than your Mom!")            
            elif mom_age <= your_age:
                print(f"What!!! you look older than your Mom")

            in_choice = input("\nBack: (y/n): ").lower()

    elif choice == "E":
        in_choice = "n"
        
        while in_choice != "y":
            print("Validation:\n")

            your_age = int(input("What is your age: "))

            if your_age >= 18:
                print("Valid")
            else:
                print("Invalid!!!")

            in_choice = input("\nBack: (y/n): ").lower()

    elif choice == "F":
        in_choice = "n"
        
        while in_choice != "y":
            print("Looping:\n")

            for i in range(10):
                if i % 2:
                    print(i)
        
            in_choice = input("\nBack: (y/n): ").lower()

print("Thank you!!!")