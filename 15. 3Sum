"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
解题思路：
首先考虑结合2Sum的解法，即固定一个数x作为基准，找其余两个数的和为-x即可，需要注意两点：
1、因为最终返回的结果是不重复的，因此考虑先用set来存放每一组数；
2、基于后来返回的是数而不是index（与2Sum的不同之处），可以先对list排序，相同的数则不用再次作为基准（无意义！）
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return []
        nums.sort()
        res = set()
        for i, x in enumerate(nums[:-2]):
            if i > 0 and x == nums[i - 1]:
                continue
            d = {}
            for y in nums[i+1:]:
                if - x - y not in d:
                    d[y] = 1
                else:
                    res.add((x, y, -x - y))
        return map(list, res)
