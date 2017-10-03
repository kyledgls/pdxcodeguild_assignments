print('Welcome to your grade calculator')

grade = input('What was your percentage? ')
percent = int(grade)
if percent <= 59:
    print('F')
elif percent >= 60 and percent <= 69:
    print('D')
elif percent >= 70 and percent <= 79:
    print('C')
elif percent >= 80 and percent <= 89:
    print('B')
else:
    print('A')