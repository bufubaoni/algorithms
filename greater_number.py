class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        ln = len(nums)
        res = [-1] * ln
        
        double = nums + nums
        for idx, item in enumerate(double):
            while stack and nums[stack[-1]] < item:
                res[stack.pop()] = item
            if idx < ln:
                stack.append(idx)
        return res