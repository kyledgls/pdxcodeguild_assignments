'''
Lets make change
'''
# welcomes user to program
print('Let\'s make CHANGE!')

# inputs the amount and stores it
cents = input('How many pennies ' )
cents = int(cents)
# calculates the change
quarters = (cents // 25)
cents -= quarters * 25
dimes = (cents // 10)
cents -= dimes * 10
nickle = (cents // 5)
cents -= (nickle * 5)
penny = (cents // 1)
cents -= (penny * 1)
# prints the result
print( 'Quarters', + quarters  ,'dimes',  dimes , 'nickles', nickle ,'pennies', penny)
