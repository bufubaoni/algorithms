# 二分法 统计nums中1的个数
nums = [1,1,1]
def count(nums):
    l = 0
    r = len(nums)
    while l<r:
        mid = (r+l)/2
        if nums[mid] == 1:
            l = mid + 1
        else:
            r = mid
    return l

print count(nums)
print sum(nums)