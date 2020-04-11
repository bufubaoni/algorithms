from bisect import bisect_right
from random import randint

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.weight = [0]
        self.s = 0

        for item in w:
            self.s+=item
            self.weight.append(self.s)
        self.s -= 1

    def pickIndex(self):
        """
        :rtype: int
        """
        w=randint(0, self.s)
        return bisect_right(self.weight,w)-1