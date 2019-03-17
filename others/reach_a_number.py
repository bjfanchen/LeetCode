"""
You are standing at position 0 on an infinite number line. There is a goal at position target.
On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.
Return the minimum number of steps required to reach the destination.
Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
思路：
1、target=a 或target=-a 结果相同
2、考虑一直正向（向右）的情况，如果其中的某次向左，记为-n，则与一直向右的情况二者相差2n，
因此找出正向走第一个超出target值为偶数的数字，该偶数记为m，则只需将第m/2步方向调换一下即可达到target！
"""
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target == 0:return 0
        temp = 0
        count = 1
        while count > 0:
            temp += count
            if temp >= abs(target) and (temp - abs(target)) % 2 == 0:
                return count
            count += 1
        
