import random
x = random.randint(1, 10)
last_guess = 0
while True:
    guess = int(input('Make a guess: '))
    if guess == x:
        print('Well done!!')
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

