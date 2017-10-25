import random



def random_list(n):
    nums = []
    for i in range(n):
        nums.append(random.randint(1, 100))
    return nums

def shuffle_nums(nums):
    for i in range(len(nums)):
        j = random.randint(0, len(nums)-1)

        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t

def is_sorted(nums2):
    for i in range(len(nums2) - 1):
        if nums2[i] > nums2[i + 1]:
            return False
    return True

def bogo_sort(nums):
    while is_sorted(nums) != True:
        shuffle_nums(nums)
    else:
        print('Sorted!')



nums = random_list(10)
bogo_sort(nums)
print(nums)
print(shuffle_nums(nums))
print(is_sorted(nums))

