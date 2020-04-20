class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        pre = ListNode(0)

        pre.next = head
        lst = []
        while head:
            lst.append(head)
            head = head.next
            lst[-1].next = None
        if not lst:
            return pre.next
        first = lst.pop(0)

        res = first
        while lst:
            
            r = lst.pop()
            first.next = r
            if not lst:
                break
            l = lst.pop(0)
            r.next = l
            first = r.next

        return res