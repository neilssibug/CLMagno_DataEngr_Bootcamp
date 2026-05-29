#print("Hello World!")
import time

choice = ""

while choice != "X" :
    print("Hello World!")
    print("\nMenu:")

    print("[A] Variables")
    print("[B] Type cast & Transform")
    print("[C] Math operations")
    print("[D] Logical operations")
    print("[E] Validation")
    print("[X] Exit")


    time.sleep(1)
    choice = input("\nChoose: ").upper()

    if choice == "A":
        in_choice = "n"
        
        while in_choice != "y":
            print("Variables:\n")
            is_string = "Welcome to Variables"
            is_integer = 10
            is_float = 1.5
            is_boolean = True

            print(f"This is a {type(is_string)} : {is_string}")
            print(f"This is a {type(is_integer)} : {is_integer}")
            print(f"This is a {type(is_float)} : {is_float}")
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

            in_choice = input("\nBack: (y/n): ").lower()

    elif choice == "C":
        in_choice = "n"
        
        while in_choice != "y":
            print("Math operations:\n")

            in_choice = input("\nBack: (y/n): ").lower()

    elif choice == "D":
        in_choice = "n"
        
        while in_choice != "y":
            print("Logical operations:\n")

            in_choice = input("\nBack: (y/n): ").lower()

    elif choice == "E":
        in_choice = "n"
        
        while in_choice != "y":
            print("Validation:\n")

            in_choice = input("\nBack: (y/n): ").lower()

print("Thank you!!!")