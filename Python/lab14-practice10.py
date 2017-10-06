



def extract_less_than_ten(nums1):
    nums2 = []

    for num in nums1:
        if num < 10:
            nums2.append(num)
        print(nums2)

    return nums2


nums1 = [3, 5, 4, 6, 2, 12]
nums2 = extract_less_than_ten(nums1)
print(nums2)