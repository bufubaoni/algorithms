class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        hs = {}
        pre = Node(-1)
        first = pre
        
        p = head
        while p:
            if p.val not in hs:
                hs[id(p)] = Node(p.val)
                nd = hs[id(p)]
            else:
                nd = hs[id(p)]
            pre.next = nd
            pre = pre.next
            p = p.next
        re = head
        c = first.next

        while re:
            if re.random:
                c.random = hs[id(re.random)]
            c = c.next
            re = re.next

            
        return first.next