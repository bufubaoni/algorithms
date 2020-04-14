# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stacka=[]
        stackb=[]

        while l1:
            stacka.append(l1.val)
            l1 = l1.next

        
        while l2:
            stackb.append(l2.val)
            l2 = l2.next
        
        c = 0
        nxt = None
        while stacka or stackb or c:
            b = 0
            a = 0
            if stackb:
                b = stackb.pop()
            if stacka:
                a = stacka.pop()

            res = (a + b + c) % 10
            c = (a + b + c) / 10
            current = ListNode(res)
            current.next = nxt
            nxt = current
        return nxt