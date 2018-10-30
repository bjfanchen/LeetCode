"""
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
题解：
实际上是一个26进制数的问题
注意：字符转ASCII码：
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        strlen = len(s)
        for i, ch in enumerate(s):
            res += (ord(ch) - ord("A") + 1) * 26 ** (strlen - i - 1)
        return res
