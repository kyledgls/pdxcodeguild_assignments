print('Welcome to the credit card validator')


# defines the function
def credit_valid():
    card = input('Input credit card: ')
    card = card.replace(' ', '')
    card = list(card)
    # removes the last character in the card number
    for i in range(len(card)):
        card[i] = int(card[i])
    numcheck = card.pop(15)
    # reverses the card numbers
    card.reverse()
    # multiplies every other indicies by two
    for i in range(0, len(card), 2):
        print(card, i)
        card[i] *= 2
    total = 0
    # subtracts all values over 9 by 9
    for i in range(len(card)):
        if card[i] > 9:
            card[i] -= 9
        total += card[i]
    # verifies the last digit with the sum of all numbers by checing the second digit
    ones_digit = total % 10
    if numcheck == ones_digit:
        print('Valid!')
    else:
        print('CUT UP THE CARD!')

credit_valid()













