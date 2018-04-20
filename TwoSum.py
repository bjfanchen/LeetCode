# -*- coding: utf-8 -*
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

一句话描述题目：
两个数之和已知target，从list中找出这两个数

解题思路：
1.两次遍历，每两个数都相加一次，再比较. 可行，但时间复杂度太高，约为O(n^2)
2.利用HashTable来实现，一次遍历list，迭代list元素将其添加进HashTable中，
  同时查找（通过in关键字来实现）table中已有元素与当前元素之和是否为target，查找成功即返回

时间复杂度：O(n)
空间复杂度：
"""


# 代码实现
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:  # 使用in查询指定键值是否存在于dict中
                return [d[m], i]
            else:
                d[n] = i


