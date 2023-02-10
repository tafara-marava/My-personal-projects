print('Welome to the pizza bill calculator ')
print()
size = input('Which size pizza do you want? S, M or L? ')

bill = 0

if size == "S":
    bill += 6
elif size == "M":
    bill += 9
elif size == "L":
    bill += 12

toppings = input('What toppings would you like on your pizza? Pineapple, Pepperoni or Sausage? ')

if size == "S":
    if toppings == "Pineapple":
        bill += 2.5
    elif toppings == "Pepperoni":
        bill += 1.8
    elif toppings == "Sausage":
        bill += 1.5
elif size == "M":
    if toppings == "Pineapple":
        bill += 2.87
    elif toppings == "Pepperoni":
        bill += 2.21
    elif toppings == "Sausage":
        bill += 1.74
elif size ==  "L":
    if toppings == "Pineapple":
        bill += 3.15
    elif toppings == "Pepperoni":
        bill += 2.43
    elif toppings == "Sausage":
        bill += 2.13

print(f'Your final bill is {bill:.2f}. Thank you for your purchase! ')