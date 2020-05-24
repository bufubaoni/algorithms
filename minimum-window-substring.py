from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        need = Counter(t)
        window = dict.fromkeys(need.keys(), 0)
        valid, L, R, ans = 0, 0, 0, (-1, len(s))
        while R < len(s):
            c = s[R]
            R += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                ans = (L, R) if R - L < ans[1] - ans[0] else ans
                c = s[L]
                L += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        if ans[0] == -1:
            return ""
        return s[ans[0]:] if ans[1] == len(s) else s[ans[0]:ans[1]]
