print('Welcome to the credit card validator')



def credit_valid():
    card1 = input('Input credit card: ')
    card1 = card1.replace(' ', '')
    card1 = list(card1)
    for i in range(len(card1)):
        card1[i] = int(card1[i])

    numcheck = card1.pop(15)
    card1.reverse()
    for i in range(0, len(card1), 2):
        #print(card1, i)
        card1[i] *= 2
    for i in range(len(card1)):
        if card1[i] > 9:
            i -= 9

    for i in range(len(card1)):
        i += len(card1)
        if numcheck == card1[1]:
            print('Valid!')
    else:
        print('CUT UP THE CARD!')

credit_valid()













