'''
Lets make change
'''

print('Let\'s make CHANGE!')

cents = input('How many pennies ' )
cents = int(cents)
quarters = (cents // 25)
cents -= quarters * 25
dimes = (cents // 10)
cents -= dimes * 10
nickle = (cents // 5)
cents -= (nickle * 5)
penny = (cents // 1)
cents -= (penny * 1)
print( 'Quarters', + quarters  ,'dimes',  dimes , 'nickles', nickle ,'pennies', penny)
