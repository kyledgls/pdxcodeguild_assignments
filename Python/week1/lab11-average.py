'''
welcome to the average show
'''

nums = [5, 0, 8, 3, 4, 1, 6]

total = 0
i = 0
while i < len(nums):
    total += nums[i]
    i += 1

print(total / len(nums))
