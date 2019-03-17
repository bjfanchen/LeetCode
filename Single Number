# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# 解题思路：
# 主要是理解按位异或的思想：同则抵消，与0异或保持不变
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res
