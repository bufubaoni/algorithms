class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        if num / 10 > 0:
            k = 0
            while num > 0:
                k += num % 10
                num = num/10
            return self.addDigits(k)
        else:
            return num
