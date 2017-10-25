import random

print('Welcome to the password generator')

x = '123456789ABCDEFGHIJKLMNOPQURSTUV!@#$%^&*()'
i = 0
password = ''
while i < 12:
    password += (random.choice(x))
    i += 1
random.choice(x)
print(password)




