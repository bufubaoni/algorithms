class Solution(object):

    def heapify(self, heap, n, i):
        p = i
        l = 2 * p + 1
        r = 2 * p + 2

        mx = i

        if l < n and heap[l] > heap[mx]:
            mx = l
        if r < n and heap[r] > heap[mx]:
            mx = r
        if mx != i:
            heap[mx], heap[i] = heap[i], heap[mx]
            self.heapify(heap, n, mx)
    
    def build(self, heap, n):
        p = n / 2
        for i in range(p-1, -1, -1):
            self.heapify(heap, n, i)
    
    
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # nums.sort(reverse=True)

        # return nums[k-1]
        ln = len(nums)
        self.build(nums, ln)
        idx = 0
        for i in range(ln-1, -1, -1):
            idx += 1
            if idx == k:
                return nums[0]
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)
        return k
