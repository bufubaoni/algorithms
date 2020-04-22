class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        o = head
        p = head.next
        e = p
        while o.next and e.next:
            o.next = e.next
            o = o.next
            e.next = o.next
            e = e.next
        
        o.next = p
        return head
        