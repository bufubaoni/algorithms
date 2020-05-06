class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [0] * len(prices)

        mi = prices[0]
        for idx in range(1, len(prices)):
            dp[idx] = max(dp[idx-1], prices[idx]-mi)
            mi = min(prices[idx], mi)
        return dp[-1]