import random

num = int(input('choose a number: '))

while True:
    x = random.randint(1, 10)
    if guess == x:
        print(x)
        break
    elif last_guess != 0:
        print('Failure will not be tolerated')
        current_difference = abs(guess - x)
        last_difference = abs(last_guess - x)
        if current_difference > last_difference:
            print('Getting colder')
        elif current_difference < last_difference:
            print('Getting Warmer')
    last_guess = guess
