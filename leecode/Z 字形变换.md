#   Z 字形变换
[Z 字形变换](https://leetcode-cn.com/problems/zigzag-conversion/) 

将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
```
L   C   I   R
E T O E S I I G
E   D   H   N
```
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:
```
L     D     R
E   O E   I I
E C   I H   N
T     S     G
```

```
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        list_s = []
        cour = 0
        if numRows == 1:
            return s
        for idx, item in enumerate(s):
            if idx % (numRows-1) == 0:
                list_s.append(s[cour + idx:cour + idx + numRows])
                cour = cour + numRows - 1
            else:
                pre_blank = []
                after_blank = []
                for item in range(numRows - 1 - (idx % (numRows - 1))):
                    pre_blank.append(" ")
                for item in range(numRows - len(pre_blank) - 1):
                    after_blank.append(" ")
                str_pre_blank = "".join(pre_blank)
                str_after_blank = "".join(after_blank)
                list_s.append(str_pre_blank + s[cour + idx:cour + idx + 1] + str_after_blank)
                cour = cour + 1 - 1
            if cour + idx +1>= len(s):
                break
        print list_s
        r_str = []
        for idx in range(numRows):
            col = []
            for item in list_s:
                if len(item) > idx and item[idx] != ' ' :
                    col.append(item[idx])
            r_str.append(''.join(col))
            col = []
        
        return ''.join(r_str)
```

思路很简单 将矩阵翻转 然后获得 然后按列遍历即可
#leecode-cn/中等