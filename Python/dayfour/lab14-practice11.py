


def combine(nums1, nums2):
    num = []
    for i in range(len(nums1)):
        num.append(nums1[i])
        num.append(nums2[i])
    return num



nums1 = [3, 6, 8, 10, 24, 18, 29]
nums2 = [4, 5, 7, 11, 23, 19, 28]



print(combine(nums1, nums2))











