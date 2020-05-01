class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """

        hash = {}
        hash[0] = 0
        res = 0
        sum = [0 for i in range(len(hours)+1)]
        for i in range(len(hours)):
            if hours[i]>8:
                sum[i+1] = sum[i]+1    
            else:
                sum[i+1] = sum[i]-1
            if sum[i+1] not in hash:
                hash[sum[i+1]] = i+1
            if sum[i+1]-1 in hash:
                res = max(res, i+1-hash[sum[i+1]-1])
            if sum[i+1]>0:
                res = max(res, i+1)
        return res
