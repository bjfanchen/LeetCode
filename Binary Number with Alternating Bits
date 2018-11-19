"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
题意：给定正数，判断其二进制是否相邻位均不同，同返回true，否则false
解题思路：
思路1. 首先转化为二进制bin(),得到一个字符串，相邻位alternating表明字符串中不存在“00”或者“11”这样的子串
思路2. >> 向右移1位，与原数进行按位异或^，如果符合题意，异或结果应该是全为1（二进制），然后加一，最高位进1，后面全为0，进行按位与，得0
"""
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # s = bin(n)
        # return '00' not in s and '11' not in s
        num = n ^ (n >> 1)
        return not(num & (num + 1))
