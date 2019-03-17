"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
Example 1:Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
题意：数组中相同元素最多的个数作为度（degree），找出与原数组度相同的最小子数组
思路：
1.考虑遍历数组，将元素值作为key，index作为value，生成一个dict（注：value是一个list）
2.遍历数组的过程中，也可得到原数组的degree
3.对新生成的dict进行遍历，如果value的长度与degree相等，即可将其列入最后比较
"""
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        deg = 0
        res = float('inf')
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = []
            d[num].append(i)
            deg = max(deg, len(d[num]))
        
        for num, indices in d.items():
            if len(d[num]) == deg:
                res = min(res, indices[-1]-indices[0]+1)
        
        return res
        
                
