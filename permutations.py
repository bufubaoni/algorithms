class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        
        res = []
        for x in nums:
            ys = nums + []
            ys.remove(x)
            for y in self.permute(ys):
                res.append([x] + y)
        return res

# result = []
# def backtrack(路径, 选择列表):
#     if 满足结束条件:
#         result.add(路径)
#         return
    
#     for 选择 in 选择列表:
#         做选择
#         backtrack(路径, 选择列表)
#         撤销选择