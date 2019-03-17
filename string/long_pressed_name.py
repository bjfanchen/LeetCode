"""
Your friend is typing his name into a keyboard.  
Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard.  
Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
思路：“双指针”
1、从两个string的头部开始比较，如果第一个字符相同则i+1，否则直接返回false(j==0)
2、i+1后，进入第二轮循环，递归比较之后的字符，如果字符对应相同则i+1进入下一轮比较，
如果不相同，则比较typed[i]与typed[i-1]是否相同，相同表明是重复不做任何操作，不相同返回false
3、当比较到name的最后一个元素后（i==len(name)）,只用判断typed的剩余字符是否是全部重复的
4、如果没返回false跳出循环则只有一种可能：j == len(typed)，即比较到了typed的最后一个元素，
有可能此时i!=len(name)，说明name后的元素无匹配，则返回false，否则true
"""
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)
