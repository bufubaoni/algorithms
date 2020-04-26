class Solution(object):
    new = ListNode("-inf")
    def merge(self, L, R):
        new = self.new
        res = new
        while L and R:
            if L.val < R.val:
                new.next = L
                L = L.next
            else:
                new.next = R
                R = R.next
            new = new.next

        while L:
            new.next = L
            L = L.next
            new = new.next

        while R:
            new.next = R
            R = R.next
            new = new.next
        return res.next
        
    def getMid(self, head):
        fast = head
        slow = head
        if not slow.next:
            return slow

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if slow.next.next:
            tmp = slow.next
            slow.next = None
            return tmp

        if not slow.next.next:
            tmp = slow.next
            slow.next = None
            return tmp

    def mergetSort(self,head):
        if not head.next:
            return head
        L1 = head
        M1 = self.getMid(head)
        L2 = self.mergetSort(L1)
        M2 = self.mergetSort(M1)
        res = self.merge(L2, M2)
        return res

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head
        res = self.mergetSort(head)
        return res
