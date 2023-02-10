print('welcome to the tip calculator')

bill = float(input('What was the total bill? $'))
tip = float(input('What percentage tip would you like to give? $'))
people = int(input('How many people to split the bill? $'))

tip_amt = bill * (tip/100)
share = (tip_amt + bill) / people 

print(f'Each person should pay: ${share:.2f}')