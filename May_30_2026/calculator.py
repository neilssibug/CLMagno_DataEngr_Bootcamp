import calc_func

def validate_value(a):
    if not a and a >= 0:
        return True
    else: False

def main():
    choice = 0

    while choice != 5:
        print("--- CLI Calculator ---\n")
        print("1. Add | 2. Subtract | 3. Multiply | 4. Divide | 5. Exit")
    
        choice = int(input("Select operation (1 - 5) :"))

        # Input Values a & b
        value_a = int(input("Enter first number :"))
        
        # var = validate_value(value_a)
        # print(f"{var}")
        # if not validate_value(value_a):
        #     value_a = int(input("Enter first number :"))

        value_b = int(input("Enter Second number :"))

        if choice == 1 :
            print("--- Addition ---")


if __name__ == "__main__":
    main()