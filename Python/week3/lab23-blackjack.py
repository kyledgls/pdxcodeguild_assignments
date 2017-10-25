card_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'A': 1, 'J': 10, 'Q': 10, 'K': 10}
print('Welcome to your black jack advisor!')



x = input('Tell me your first card: ').upper()
y = input('Tell me your second card: ').upper()
z = input('Tell me your third card: ').upper()

x = card_dict[x]
y = card_dict[y]
z = card_dict[z]

n = sum([x,y,z])
print(n)
if n <= 17:
    print('Hit!')
elif n < 21:
    print('Stay!')
elif n == 21:
    print('BlackJACK!!!!!')







