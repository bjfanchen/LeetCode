"""
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.
Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
题意：给定字符串，找出符合题意的字串的个数：1、子串中的1的个数和0的个数正好相等；2、1和0都必须连续；3、子串值可以相同
思路：
由于连续性，考虑“压缩”的思想，只记录连续元素的个数:
00110011 ——> 2222  0011、01、1100、10、0011、01  6 = max(2,2)+max(2,2)+max(2,2)
1101111 ——> 214  10、01  2 = max(2,1) + max(1,4)
10101 ——> 11111  10、01、10、01  4 = max(1,1)+max(1,1)+max(1,1)+max(1,1)
"""
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        chunks, consecutive, res = [], 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                consecutive += 1
            else:
                chunks.append(consecutive)
                consecutive = 1
        chunks.append(consecutive)
        for j in range(1, len(chunks)):
            res += min(chunks[j-1], chunks[j])
            
        return res
