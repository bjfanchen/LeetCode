"""
We are given two strings, A and B.
A shift on A consists of taking string A and moving the leftmost character to the rightmost position. 
For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. 
Return True if and only if A can become B after some number of shifts on A.
Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true
Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
解题思路：
1、实际上是一个循环移位的问题。每次向左移动一位，比较结果，若相同则返回true，整体移动一次后，不相同返回false
2、另一个思路是：若B是A循环移位得到的，则二者长度必然相等，另外B必定是A+A的子串
"""
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # if A == B:return True
        # if len(A) != len(B):return False
        # for i in range(len(A)):
        #     A = A[1:] + A[0]
        #     if A == B:return True
        # return False
        return len(A) == len(B) and B in (A + A)
