class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for n in range(4, n+1):
            mx = 0
            for j in range(1, n/2+1):
                mx = max(mx, dp[j] * dp[n-j])
            dp[n] = mx
        return dp[n]
