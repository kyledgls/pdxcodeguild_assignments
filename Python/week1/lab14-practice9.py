




nums1 = [3, 5, 4, 6, 2, 12]
nums2 = [4, 6, 2, 7, 9, 12]


def common_elements(nums1, nums2):
    matches = []
    for num in nums1:
        if num in nums2:
            matches.append(num)
    return(matches)

print(common_elements(nums1, nums2))
