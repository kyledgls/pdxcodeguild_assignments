#pick six by Kyle Douglas
import random

def picksix():

    nums1 = []
    for i in range(6):
        nums1.append(random.randint(1, 99))
    return nums1


def calculate_pay_off(winning_nums, ticket):
    matches = 0
    for i in range(6):
        if winning_nums[i] == ticket[i]:
            matches += 1
    if matches == 1:
        return 4
    elif matches == 2:
        return 7
    elif matches == 3:
        return 100
    elif matches == 4:
        return 50000
    elif matches == 5:
        return 1000000
    elif matches == 6:
        return 250000000
    return 0



cost = 0
winnings = 0



# pick out six random numbers for the 'winners'

winning_nums = picksix()

# loop like 100,000 times
for i in range(100000):
    cost += 2
    ticket = picksix()
    winnings += calculate_pay_off(winning_nums, ticket)


print(f"You've spent ${cost} on tickets.")
print(f"Your earnings so far are ${winnings}.")












