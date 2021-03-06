class Solution(object):
    def waysToChange(self, n):
        coins = [1,5,10,25]
        dp = [0]*(n + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, n+1):
                dp[i] = dp[i] + dp[i - coin]
        return dp[-1] % 1000000007