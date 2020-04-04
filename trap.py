class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        # 使用动态规划 只记录右极限

        max_l = 0
        max_r = [0] * len(height)
        for idx in range(len(height)-2,-1, -1):
            max_r[idx] = max(height[idx+1], max_r[idx + 1])
        res = 0
        for idx in range(1, len(height)):
            max_l = max(height[idx-1], max_l)
            mi = min(max_l, max_r[idx])
            if mi > height[idx]:
                res += (mi - height[idx])
        return res