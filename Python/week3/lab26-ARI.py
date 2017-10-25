import math




# opens the file
with open("11-0.txt", "r") as file:
    contents = file.read()
    # lowers the case of the characters for uniformity
    contents = contents.lower()
    # replaces new line with a space
    contents = contents.replace('\n', ' ')
    # replaces ?! with periods to count sentences
    contents = contents.replace('!', '.')
    contents = contents.replace('?', '.')
    # divides the contents by spaces between periods
    sentences = contents.split(".")
    # counts the sentences
    sentence_count = len(sentences)
    for char in ",.:;'\"[]{}()!?":
        contents = contents.replace(char, '')
        # counts the words
    words = contents.split(' ')
    word_count = len(words)
    # counts the characters
    char_count = 0
    for char in contents:
        if char in 'abcdefghijklmnopqrstuvwxyz1234567890':
            char_count += 1

# calculates the ari score
ari_calc = math.ceil(4.71 * (char_count/word_count) + 0.5*(word_count/sentence_count) - 21.43)

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

grade_level = ari_scale[ari_calc]
print(grade_level)


print('CHARACTER COUNT', char_count)
print('WORD COUNT', word_count)
print('SENTENCE COUNT', sentence_count)
#prints a summary of the books ARI info
print(' --------------------------------------------------------\n', 'The ARI for', 'Alice in Wonderland', 'is', ari_calc, '\n This corresponds to a', ari_scale[ari_calc]['grade_level'], 'of difficulty', '\n that is suitable for an average person', ari_scale[ari_calc]['ages'], 'years old.\n', '--------------------------------------------------------')




