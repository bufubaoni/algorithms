class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0 or (num&(num-1)):
            return False
        return (num - 1) % 3 == 0

# 4的幂次方 -1 都是 3的倍数

# 4 的幂次方刚好落在偶数位置
