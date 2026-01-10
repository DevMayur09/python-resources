# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

running = True

while running:
    number = int(input("Enter a number: "))

    if(number < 1 ):
        print("Invalid input. Please enter a positive number")
        continue

    for i in range(1,11):
        if (i == 5):
            continue
        print(f"{number} * {i} = {number * i}")
    
    want_to_continue = input("Do you want to continue?(yes/no)")
    if want_to_continue.lower() == "no":
        running = False
    elif want_to_continue.lower() == "yes":
        continue
    else:
        print("Invalide Input. Please enter yes or no")
        continue



