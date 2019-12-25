class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0]*(n+1)

        dp[1] = 1
        dp[2] = 2

        c1 = 1
        c2 = 2
        res = 0
        for i in range(3, n+1):
            res = c1+c2
            c1 = c2
            c2 = res
        return res