# -*- coding: utf-8 -*
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
一句话描述题目：
和最大的子数组

解题思路：
这是一个优化问题，可以采用DP算法，因此需要分析本次计算与上一次计算之间的联系。
假设我们需要计算n个元素的最大子数组，直接计算可能无从下手。但如果已经计算出前n-1个元素的数组的最大子数组，那么问题可以简化为：
maxSubArray(n)=max{ maxSubArray(n-1), arr[n], maxSubArray(n-1) + arr[n] }
注：最后一种情况又比较复杂，可以直接相加进行比较的情况是：上一次计算得到的最大子数组包括了最后一个元素！！！
因此需要再设定一个变量标记上一次计算中与下一个元素相邻的最大子数组。。。

"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for i in nums[1:]:
            curSum = max(i, curSum + i)  # curSum作用：标注与下一个元素相邻的最大子数组（不一定是整个数组的最大子数组）
            maxSum = max(maxSum, curSum)
            # maxSum用于选出上一次的最大子数组与curSum中的最大值（因为上一次的最大子数组与下一次循环添加的元素不一定相邻）

        return maxSum
