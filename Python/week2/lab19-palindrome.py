


def check_palindrome():
    word = input('Input a word: ')
    if (word[::-1]) == word:
        print('Palindrome!')
    else:
        print('Not a Palindrome!')



check_palindrome()
