class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
    
        res = []
        stack = []
        tmp =''
        for item in S:
            if item == '(':
                if not stack:
                    tmp = ''
                else:
                    tmp += item
                stack.append(item)
            elif item == ')':
                stack.pop()
                if not stack:
                    res.append(tmp)
                else:
                    tmp += item
        return ''.join(res)