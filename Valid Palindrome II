"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
解题思路：
双指针，分别从字符串的两头开始，依次向内递进比较，
如果遇到不同的情况，将其中任意一个字符删除，比较中间剩余的字符串是否是回文
如果是，则返回true，否则false
如果比较循环结束，未返回任何结果，说明整个字符串本身就是回文，返回true
"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left+1:right+1]
                return one[::-1] == one or two[::-1] == two
            left += 1
            right -= 1
        return True
