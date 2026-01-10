#Problem: Calculate the sum of even numbers up to a given number n.

running = True

while running:
    n = int(input("Enter a Number(1-10000)"))

    if(n < -1 or n > 10000):
        print("Invalid Input. Please provide number between 1-10000")
        continue

    sum_of_evens = 0
    for num in range(1, n+1):
        if num % 2 == 0:
            sum_of_evens += num
    
    print(f"Sum of even numbers up to {n} is: {sum_of_evens}")

    want_to_continue = input("Do you want to continue? (yes/no)")
    if want_to_continue.lower() == "no":
        running = False
    elif want_to_continue.lower() == "yes":
        continue
    else:
        print("Invalid Input. Please enter yes or no")
        continue
        
