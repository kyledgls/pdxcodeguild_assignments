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

    pair_set = {}
    for i in range(len(words) - 1):
        if words[i] == '' or words[i + 1] == '':
            continue
        word = words[i] + " " + words[i + 1]
        if word in pair_set:
            pair_set[word] += 1
        else:
            pair_set[word] = 1
    #print('Here is the word set: ', pair_set)

    words = list(pair_set.items())
    words.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(words))):
        print(words[i])

