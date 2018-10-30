"""
一句话说明题意：
给定非负数组，只有不相邻的元素可以相加，求最大和
题解：
分析如下：
f(0) = nums[0]
f(1) = max(nums[0], nums[1])
f(k) = max(nums[k] + f(k-2), f(k-1))
此题明显是一个DP问题，当前解与前两步相关，
结合fabonacci数列实现方法，实现过程如下：
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        
        for i in nums: 
            last, now = now, max(last + i, now)
                
        return now
        
