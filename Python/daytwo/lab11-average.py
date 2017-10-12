'''
welcome to the average show
'''

nums = [5, 0, 8, 3, 4, 1, 6]

len(nums)
average = 0
i = 0
while i < len(nums):
    average += nums[i]
    i += 1

average / len(nums)
print(average / len(nums))
