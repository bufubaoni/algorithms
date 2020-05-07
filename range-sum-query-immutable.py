class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.data = [0]

        for idx in range(len(nums)):
            self.data.append(nums[idx] + self.data[idx])
        
        # print self.data

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.data[j+1] - self.data[i]