class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n

        while l <r:
            mid = (l+r)/2
            if guess(mid) == 1:
                l = mid+1
            elif guess(mid) == 0:
                return mid
            else:
                r = mid
        return l
# 这是一道非常典型的二分查找问题
# 如果小于 左区间右移，
# 如果大于 右区间左移
