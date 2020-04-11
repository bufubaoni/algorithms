class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) / 2
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid
        return l

# 由于是在n+1 范围内， 1 -> n 所以根据根绝和来判断是否有重复的数字
