rental = input('What kind of rental car would you like?')
print(f'Let me see if i can find you a {rental.title()}')

guests = input('How many people will be dining?')
guests = int(guests)
if guests > 8:
    print('Please stand by and wait for a table.')
else:
    print("Your table is ready")

number = input('Guess a number')
number = int(number)
if number % 10 == 0:
    print('This number is a multiple of 10')
else:
    print('This number is not a multiple of 1')