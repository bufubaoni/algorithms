class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        pre = [0] * (len(A) + 1)
        kcnt = [0 for i in range(K)]
        for idx, item in enumerate(A):
            pre[idx+1] = pre[idx] + item

        for item in pre:
            kcnt[item % K] += 1
        # cn 2 n 个中选出两个， 如果相加可以被k整除，那么两数mod k相等
        return sum(x * (x-1)//2 for x in kcnt)
