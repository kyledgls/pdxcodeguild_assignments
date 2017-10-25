

def cipher(text):
    english = 'abcdefghijklmnopqrstuvwxyz '
    rot =     'nopqrstuvwxyzabcdefghijklm '
    for char in text:
        #print(char)
        #print(english.find(char))
        x = english.find(char)
        print(rot[x])




text = input('Tell me a message: ')
encoded_text = cipher(text)
print(encoded_text)

