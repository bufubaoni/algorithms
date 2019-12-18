class NumArray(object):
    def build_tree(self, arr, tree, n, start, end):

        if start == end:
            tree[n] = arr[start]
        elif end == -1:
            tree = []
        else:
            p = n 
            node_left = 2 * p + 1
            node_right = 2 * p + 2
            mid = (start + end) / 2
            self.build_tree(arr, tree, node_left, start, mid)
            self.build_tree(arr, tree, node_right, mid+1, end)

            tree[n] = tree[node_left] + tree[node_right]

    def tree_len(self, arr, start, end):
        if start == end:
            return 1
        elif end == -1:
            return 1
        else:
            mid = (start + end)/ 2
            l = self.tree_len(arr, start, mid)
            r = self.tree_len(arr, mid+1, end)
            return l + r

    def update_tree(self, arr, tree, n, start, end, idx, val):
        if start == end == idx:
            tree[n] = arr[idx] = val
        else:
            node_left = 2 * n + 1
            node_right = 2 * n + 2
            mid = (start + end) /2
            if idx > mid:
                self.update_tree(arr, tree, node_right, mid + 1, end,  idx, val)
            else:
                self.update_tree(arr, tree, node_left, start, mid, idx, val)
            tree[n] = tree[node_left] + tree[node_right]

    def query_tree(self, arr, tree, n, start, end, L, R):
        if L > end or R <start:
            return 0
        elif end == start:
            return arr[start]
        elif start >= L and end <= R:
            return tree[n]
        else:
            node_left = 2 * n + 1
            node_right = 2 * n + 2
            mid = (start + end) /2

            sum_left = self.query_tree(arr, tree, node_left, start, mid, L, R)
            sum_right = self.query_tree(arr, tree, node_right, mid+1, end, L, R)
            return sum_left + sum_right

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.nums_ln = len(self.nums)
        self.tree_ln = self.tree_len(self.nums, 0, self.nums_ln-1) + self.nums_ln
        self.tree = [0] * self.tree_ln *2
        

        self.build_tree(self.nums, self.tree, 0, 0, self.nums_ln-1)


        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.update_tree(self.nums, self.tree, 0, 0, self.nums_ln-1, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # print self.tree
        return self.query_tree(self.nums, self.tree, 0, 0, self.nums_ln-1,i,j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)