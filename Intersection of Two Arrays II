"""
Given two arrays, write a function to compute their intersection.
解题思路：
先对一个array遍历进行字母频率统计，字母作为key，该字母出现次数作为value，生成一个dict
对第二个array进行遍历，若该字母出现在dict中，则将其加入最终结果，并对词频减一，最终遍历结束即可得到最终结果
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = dict()
        for i in nums1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        ret = []
        for i in nums2:
            if i in dict1 and dict1[i]>0:
                ret.append(i)
                dict1[i] -= 1
        return ret
