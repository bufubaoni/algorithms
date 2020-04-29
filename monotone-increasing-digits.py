class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        return self.get_res(N)
    
    def get_res(self, N):
        K = N
        flag = True
        while flag:
            st = str(K)
            stack = []
            for idx, item in enumerate(st):
                if stack and item < stack[-1]:
                    stack[-1] = str(int(stack[-1]) - 1)
                    st = "".join(stack) + '9'* (len(st) - idx )
                    K = int(st)
                    break
                stack.append(item)
            else:
                flag = False
        return K

# 本位减1 然后后边数字补9 