class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = nums[0]

        su = 0
        i = 0
        idx = 0
        while idx < len(nums):
            if su > 0:
                su += nums[idx]
            else:
                su = nums[idx]
                i += 1
            idx += 1
            res = max(su, res)
        return res