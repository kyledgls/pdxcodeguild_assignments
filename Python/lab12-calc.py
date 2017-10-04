
print('Welcome to a basic calculator')
operator = input("CHOOSE ONE * + / - : ")
first = int(input('SELECT FIRST NUMBER: '))
second = int(input('SELECT SECOND NUMBER: '))
float(first)
float(second)
if operator == '+':
    print(first, "+", second, "=", first + second)
elif operator == '-':
    print(first, "-", second, "=", first - second)
elif operator == "*":
    print(first, "*", second, "=", first * second)
elif operator == "/":
    print(first, "/", second, "=", first / second)
else:
    print('ERROR')