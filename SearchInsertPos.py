# -*- coding: utf-8 -*
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
一句话描述题目：
给定数值，在有序数组中查找，找到返回index，找不到返回应插入的位置

解题思路：
对数组遍历进行查找，找到返回index
由于数组有序，若发现遍历时某个元素比target大，则该数组中不存在该元素，返回index
以上两种情形可以合并
另外需要考虑到，若target比数组中最大的元素都要大，则需要将其插入到最后一个位置，即len(nums)

时间复杂度：O(n)

"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[len(nums) - 1]:
            return len(nums)

        for i, x in enumerate(nums):
            if x >= target:
                return i
