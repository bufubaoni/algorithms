class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0

        i = 1
        while n / i:
            high = n / (10 * i)
            cur = n / i % 10

            low = n - (n / i) * i

            if cur == 0:
                cnt += high * i
            elif cur == 1:
                cnt += high * i + low + 1
            else:
                cnt += (high + 1) * i

            i = i * 10

        return cnt
