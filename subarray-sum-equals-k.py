
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        cnt = 0
        su = 0
        cul = {0:1}
        for item in nums:
            su += item
            if su - k in cul:
                cnt += cul[su-k]
            re = cul.get(su, 0)
            re += 1
            cul[su] = re
        return cnt

# cul 记录 所有数字的和， 如果 之后减去k 在cul 中说明 此时之和减去 之前的小线段会得到结果