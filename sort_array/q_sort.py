# 快速排序

def qSort(nums):
    if len(nums)<2:
        return nums
    current = nums[0]
    
    left = [i for i in nums[1:] if i<=current]
    right = [i for i in nums[1:] if i>current]
    
    return qSort(left) + [key] + qSort(right) 

# 将所有小于等于第一个的数放到左边
# 大于第一个数的放到右边
# 然后拼接为一个array
# 当只有一个数字的时候结束递归
