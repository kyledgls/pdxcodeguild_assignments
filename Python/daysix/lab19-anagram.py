

print('Welcome to the Anagram detector!')

def anagram():
    line1 = input('Tell me a word: ')
    line2 = input('Tell me another word: ')
    line1 = line1.lower()
    line2 = line2.lower()
    line1 = line1.replace(' ', '')
    line2 = line2.replace(' ', '')
    line1 = list(line1)
    line2 = list(line2)
    line1.sort()
    line2.sort()
    if line1 == line2:
        print('ANAGRAM!')
    else:
        print('Not an ANAGRAM')


anagram()



