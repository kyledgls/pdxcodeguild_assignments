import random
print('Welcome to the EMOTE Jungle')
eyes = [';', ':', '8']
nose = ['<', '>', '']
mouth = [')', '(', "P"]

emote = (random.choice(eyes))
dmote = (random.choice(nose))
vmote = (random.choice(mouth))
print(emote+dmote+vmote)
