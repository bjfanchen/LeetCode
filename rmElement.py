# -*- coding: utf-8 -*
"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

一句话描述题目：
数组去掉指定元素

解题思路：
与数组去重类似，采用两个指针的形式，区别只在于i的初始值，以及if条件的操作

时间复杂度：O(n)
空间复杂度：O(1)
"""


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j