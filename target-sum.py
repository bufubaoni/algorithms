class Solution(object):
    count = 0

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if sum(nums) < S or (sum(nums) + S) % 2 == 1:
            return 0

        p = (sum(nums) + S) // 2
        dp = [1] + [0] * p
        for num in nums:
            for j in range(p, num-1, -1):
                dp[j] += dp[j - num]
        return dp[p]
