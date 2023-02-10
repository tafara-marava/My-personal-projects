age = input('What is your current age?')

death = 90
days_left = (death - int(age)) * 365
weeks_left = (death - int(age)) * 52
months_left = (death - int(age)) * 12

print(f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left.')