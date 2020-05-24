class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 1

        s = []
        while num:
            s.append(num % 10)
            num = num / 10
        s.reverse()
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1
        for idx in range(2, len(s)+1):
            if s[idx-1]+s[idx-2]*10 <= 25 and s[idx-2] != 0:
                dp[idx] = dp[idx-1] + dp[idx-2]
            else:
                dp[idx] = dp[idx-1]
        return dp[-1]
