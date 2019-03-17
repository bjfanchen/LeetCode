"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
Example:
  Input: [4,2,3]
  Output: True
  Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
一句话说明题意：修改至多一个元素使数组递增，可行返回true，否则false
题解：
题意所述方案可行的情况是指数组大部分有序，局部乱序。
需要做的就是找出乱序部分，将其中的一个元素修改为临近元素即可。
"""
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sorted(nums) == nums:return True
        one, two = nums[:], nums[:]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                one[i] = one[i+1]
                two[i+1] = two[i]
                break
        return one == sorted(one) or two == sorted(two)
    
