#input pizza order 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()
# code to pizza order 
bill = 0 
if size == 's':
    bill += 15
    if add_pepperoni == 'y':
            bill += 2
    elif extra_cheese == 'y':
                    bill += 1
elif size == 'm':
    bill += 20
    if add_pepperoni == 'y':
            bill += 3
    elif extra_cheese == 'y':
                    bill += 1
elif size == 'l':
    bill +=25
    if add_pepperoni == 'y':
            bill += 3
    elif extra_cheese == 'y':
                    bill += 1
else : 
    print("Invalid input 'plz try again !'")

print(f'Your total amount is ${bill}')

