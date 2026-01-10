running = True

while running:
    should_continue = input("Do you want to continue? (yes/no): ")
    if should_continue.lower() == "no":
        print("Thank you for using our program.")
        running = False
    elif should_continue.lower() == "yes":
        age = int(input("Enter your age: "))
        if age < 13:
            print("You are a child.")
        elif age >=13 and age < 20:
            print("You are a teenager.")
        elif age >=20 and age < 60:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
    

         