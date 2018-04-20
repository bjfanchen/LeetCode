# -*- coding: utf-8 -*
"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
一句话描述题目：
有序list去重

解题思路：
Since the array is already sorted, we can keep two pointers i and j, where i is the slow-runner while j is the fast-runner.
As long as nums[i] = nums[j], we increment j to skip the duplicate.

When we encounter nums[j]≠nums[i], the duplicate run has ended so we must copy its value to nums[i+1].
i is then incremented and we repeat the same process again until j reaches the end of array.

设定两个指针i和newTail，i用于iterate对每个元素进行检查，newTail用于标记去重过程中list的尾部( i > newTail )
当nums[i]和nums[newTail]相等时，不做任何操作，i递增
当nums[i]和nums[newTail]不等时，newTail递增，并将nums[i]赋值给nums[newTail]
当i执行到list最后一个元素，循环结束，newTail+1即是去重list元素个数
注意：1.去重后list大小不变，区别在于前（newTail+1）个元素是不重复的，后面的元素与原list相同
     2.remove实现不可行，原因在于remove掉重复元素后，list变短，原来指针指向的元素变化，可能会跳过某些元素的去重比较
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #         for i, x in enumerate(nums):
        #             if nums[i] == nums[i - 1]:
        #                 nums.remove(nums[i])

        #         return len(nums)
        if len(nums) == 0:
            return 0

        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1


"""
时间复杂度：O(n)
空间复杂度：O(1)
"""