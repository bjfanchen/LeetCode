"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
There is at least one empty seat, and at least one person sitting.
Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
Return that maximum distance to closest person.
Example 1:
Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
解题思路：
主要需要考虑连续空位的个数，个数设为zeroes：
1、假设连0在最前面，则 res = max(res, zeroes)
2、在中间，则 res = max(res, (zeroes+1)/2)
3、在末尾，则 res = max(res, zeroes)
关键点在于如何找到连续零的个数，设两个参数，一个标记0开始的位置，另一个标记0结束的位置（即连零之后的第一个1的位置）
"""
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        i, j, res, n = 0, 0, 0, len(seats)
        for j in range(n):
            # j标记连续0后的第一个1的位置，i标记0开始的位置，j-i即是连0的个数
            if seats[j] == 1:
                if i == 0:
                    res = max(res, j - i) 
                else:
                    res = max(res, (j - i + 1) / 2)
                i = j + 1
        res = max(res, n - i)
        return res
                
