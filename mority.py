class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = None
        count_a = 0

        b = None
        count_b = 0

        for item in nums:
            # print a, b, count_a, count_b
            if item == a:
                count_a += 1
                continue
            if item == b:
                count_b += 1
                continue
            
            if count_a == 0:
                a = item
                count_a = 1
                continue
            if count_b == 0:
                b = item
                count_b = 1
                continue
            
            count_a -= 1
            count_b -= 1
        ct_a = 0
        ct_b = 0
        ans = []
        ml = len(nums) / 3
        for num in nums:
            if a == num:
                ct_a += 1
            elif b == num:
                ct_b += 1
        if ct_a > ml:
            ans.append(a)
        if ct_b > ml:
            ans.append(b)
        return ans

# template
# a = None
# b = 0
# for i in range(len(A)):
#     if a == None:
#         a = A[i][j]
#         b = 1
#     elif a == A[i][j]:
#         b += 1
#     elif b == 0:
#         a = A[i][j]
#         b = 1
#     else:
#         b -= 1