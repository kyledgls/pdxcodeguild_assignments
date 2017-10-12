import random

print('Welcome to the MAGIC 8 ball!')
question = input('Ask me anything ')

predictions = ['TRY AGAIN LATER', 'NEVER', 'SOON', 'Hazy, try again', 'Most likely ', 'DEATH IS CERTAIN', '']

prediction = random.choice(predictions)
print(prediction)

i = 1
while i<1:
    print(random.choice(prediction))
    i += 1