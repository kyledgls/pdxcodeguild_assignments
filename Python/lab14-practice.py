import random





def count_letter(char_to_find, word):
    count = 0
    for i in word:
        if i == char_to_find:
            count = count+1
    print(count)


count_letter('i', 'antidisestablishmentterianism')
count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')




s = "        NANNANANANA BATMAN        "
s = s.lower()
s = s.strip()
print(s)


x = int(input('Input a number: '))
if (x % 2 == 0) :
    print("even")
elif (x % 2 == 1) :
    print("odd")



fruits = ['watermelon', 'grapefruit', 'pineapple', 'banana', 'cherry' ]
fruit = random.choice(fruits)
print(fruit)

i = 1
while i < 1:
    print(random.choice(fruit))
    i += 1

s = (5, 12, 11)
x = (5, 12, 11)
print(max(x))

def expo():
    a = 0
    while a <= 20:
        print(a ** 2)
        a += 1


expo()


def minimum(numbs):
    print(numbs)
    min_value = 100
    for numb in numbs:
        if numb < min_value:
            min_value = numb
    return min_value
print(minimum([4, 6, 2, 8, 7, 1]))



def maximum(bums):
    print(bums)
    max_value = -100000
    for bums in bums:
       if bums > max_value:
           max_value = bums
    return max_value
print(maximum([10, 43, 65, 21, 99, 25]))

# incomplete
def mean(bums):
    print(bums)
    mean_value = list+list/sum
    for bums in bums:
        if bums > mean:
            mean_value = bums
    return mean_value
print(mean([10, 43, 65, 21, 99, 25]))
















