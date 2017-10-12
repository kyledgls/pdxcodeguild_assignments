'''
this is a game of rock paper scissors.
'''
import random

# defines users and options
print('Let us play Rock Paper Scissors')
player1 = input('Choose rock, paper, or scissors ')
computer = ['rock', 'paper', 'scissors']
player2 = random.choice(computer)
print(player2)
#addresses the 9 cases of the game
if player1 == 'rock' and player2 == 'scissors':
    print('You Win!')

elif player1 == 'rock' and player2 == 'paper':
    print('computer wins, sorry!')

elif player1 == player2:
    print('a draw brings DISHONOR!')

elif player1 == 'scissors' and player2 == 'rock':
    print('You lose!')

elif player1 == 'scissors' and player2 == 'paper':
    print('You win!')

elif player1 == 'paper' and player2 == 'rock':
    print('You Win!')

elif player1 == 'paper' and player2 == 'scissors':
    print('You lose!')

elif player1 == 'paper' and player2 == 'rock':
    print('you win!')

else:
    print('invalid')





