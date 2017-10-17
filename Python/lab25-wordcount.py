print('Welcome to Alice in Wonderland\'s word count adventure!')

with open("11-0.txt", "r") as file:
    contents = file.read()
    contents = contents.lower()
    contents = contents.replace('\n', ' ')

    for char in ",.:;'\"[]{}()!?":
        contents = contents.replace(char, '')
    words = contents.split(' ')

    word_set = {}
    for word in words:
        if word == '':
            continue
        if word not in word_set:
            word_set[word] = 1
        else:
            word_set[word] += 1


print(word_set)

words = list(word_set.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])