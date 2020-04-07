class Solution(object):
    def kthSmallest(self, matrix, k):
        “””
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        “””

        # 暴力解法
        lst = sum(matrix, [])
        lst.sort()
        return lst[k-1]