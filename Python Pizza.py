print("Welcome to Python Pizza Order!")
size = input("What size pizza do you want? S, M or L:\n ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n ")
extra_cheese = input("Do you want to add extra cheese? Y or N:\n ")
bill = 0

# set prize for the pizza
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You put the wrong value!")

#Set value for the pepperoni
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
#Set value for the cheese and final bill
if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is: ${bill}.")


