class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1]
        i2 = i3 = i5 = 0

        for item in range(0, n):
            ugly = min(nums[i2]*2, nums[i3]*3, nums[i5]*5)
            nums.append(ugly)
            if ugly == nums[i2]*2:
                i2 += 1
            if ugly == nums[i3]*3:
                i3 += 1
            if ugly == nums[i5]*5:
                i5 += 1
        return nums[n-1]
