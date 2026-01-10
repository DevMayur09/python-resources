# Problem: Movie tickets are priced based on age: 
# $12 for adults (18 and over), 
# $8 for children. 
# Everyone gets a $2 discount on Wednesday.


import datetime

running = True
while running:
    today = datetime.datetime.now()
    day = today.strftime("%A")

    discount = 0
   
    if day.lower() == "sunday":
        discount = 2
    else:
        discount = 0
    
    age = int(input("Enter Your Age: "))

    if age >= 18:
        print(f"Please Pay ${12 - discount}")
    else:
        print(f"Please Pay ${8 - discount}")
    
    buy_more = input("Do you want to buy more tickets? (yes/no):")
    if buy_more.lower() == "no":
        running = False
    elif buy_more.lower() == "yes":
        continue
    else:
        print("Invalid Input, Please enter yes or no")
        continue

