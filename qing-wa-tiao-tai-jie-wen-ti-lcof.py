class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for item in range(3, n+1):
            dp[item] = dp[item-1] + dp[item-2]
        return dp[n] % 1000000007
