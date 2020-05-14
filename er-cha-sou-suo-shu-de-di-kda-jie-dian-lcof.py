class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        path = []

        self.trived(root, path)
        # path.reverse()
        return path[k-1]

    def trived(self, root, path):
        if not root:
            return
        self.trived(root.right, path)
        path.append(root.val)
        self.trived(root.left, path)
