"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
解题思路：

"""
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # res表示当前无backspace的list，ch是在res之后追加的元素
        def back(res, ch):
            if ch != "#": res.append(ch)
            elif res: res.pop()
            return res
        # reduce()函数表示将S中的每一个元素作为参数进行back()函数计算，[]是初始值，表示第一次计算是[]和S中的第一个元素，
        # back()返回结果再与S的第二个元素进行计算,依次计算
        return reduce(back, S, []) == reduce(back, T, [])
        
