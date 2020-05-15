# -*- coding: utf-8 -*-
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        cnt = 0
        su = 0
        cul = {0: 1}
        for item in nums:
            su += item
            if su - k in cul:
                cnt += cul[su-k]
            re = cul.get(su, 0)
            re += 1
            cul[su] = re
        return cnt


def get_sub(nums, k):
    # 获取连续子数组 等于k
    res = []

    su = 0
    cul = {0: [0]}

    for idx, item in enumerate(nums):
        su += item

        if su - k in cul:
            for start in cul[su-k]:
                if (start, idx) not in res:
                    res.append((start, idx))
        re = cul.get(su, [])
        re += [idx]
        cul[su] = re
    print cul
    return [nums[start:end] for start, end in res]
    # cul 记录 所有数字的和， 如果 之后减去k 在cul 中说明 此时之和减去 之前的小线段会得到结果


if __name__ == "__main__":
    print(get_sub([1, 1, 1], 2))

    print([1, 1, 1][-1:2])
