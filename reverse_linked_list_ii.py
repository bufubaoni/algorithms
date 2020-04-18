class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy

        for i in range(m):
            pre = pre.next

        curr = pre
        later = curr.next
        
        for i in range(n-m):
            tmp = later.next
            later.next = curr
            curr=later
            later = tmp
            # curr, later.next, later = later,  curr, later.next
        
        pre.next.next = later
        pre.next = curr
        return dummy.next