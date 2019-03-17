"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.
We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
Example 1:
Input: nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
题意:给定数组，找出中心点，保证中心店两边的元素和相等（不包括中心点）
思路：容易想到的就是遍历数组，但是每次求和过于复杂，考虑在遍历的过程中分别增减元素进行比较
"""
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, sum(nums)
        for index, num in enumerate(nums):
            r -= num
            if l == r:return index
            l += num
        return -1
