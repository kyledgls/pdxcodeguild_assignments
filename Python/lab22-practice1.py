


my_list = []
while True:
    my_input = input('Enter a number (or \'done\'): ')
    if my_input == 'done':
        print(my_list)
        break
    else:
        print('Incorrect file name or path')
    my_list.append(int(my_input))








