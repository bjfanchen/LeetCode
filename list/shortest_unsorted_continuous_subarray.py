"""
Given an integer array, you need to find one continuous subarray 
that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
You need to find the shortest such subarray and output its length.=
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
"""
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 列表生成式，将原list与排序后的list进行比较，同一位置的元素相同，新列表元素值为true，否则为false
        is_same = [a == b for a, b in zip(nums, sorted(nums))] 
        return 0 if all(is_same) else len(is_same) - is_same[::-1].index(0) - is_same.index(0)
        # 如果is_same元素全为true则说明原数组有序返回0
        # 否则，需要找出is_same的第一个false和最后一个false，即子数组的头和尾，长度为（尾-头+1）
        # 尾部index通过反转列表来找，注意返回的是反转列表后的index，二者的关系是和为length-1
        # 因此是(len - 1 - is_same[::-1].index(false)) - is_same.index(false) + 1
