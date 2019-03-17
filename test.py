# -*- coding: utf-8 -*
# import re
#
#
# def checkip(ip):
#     check = re.compile(r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
#     if check.match(ip):
#         return True
#     else:
#         return False
#
#
# myStr = "255.255.255.300"
# if checkip(myStr):
#     print(myStr, "is a IP address")
# else:
#     print(myStr, "is not a IP address")
#
#
# myStr1 = "my " + "pencil"
# myStr2 = "...".join(("www", "baidu", "com"))
# print(myStr1)
# print(myStr2)

#
# def demo(lst, k):
#     x = lst[:k]
#     x.reverse()
#     y = lst[k:]
#     y.reverse()
#     r = x+y
#     return list(reversed(r))
#     # return y + x
#
#
# def demo1(lst, k):
#     temp = lst[:]
#     for i in range(k):
#         temp.append(temp.pop(0))
#     return temp
#
#
# mylst = [1, 2, 3, 4, 5]
# print(demo(mylst, -3))
# print(demo1(mylst, 19))

#
# li = [2, 3, 4, 5, 1, 2, 3]
# new_li = list(set(li))
# new_li.sort(key=li.index)
# print(new_li)
#
#
# my_set = {1, 1, 1, 3, 2}
# print(my_set)


# class Node(object):
#     def __init__(self, data, left, right):
#         self.data = data
#         self.left = left
#         self.right = right
#
#
# def preVisit(Node):
#     if Node:
#         print(Node.data)
#         preVisit(Node.left)
#         preVisit(Node.right)

# 判断回文链表的错误做法！！！
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution(object):
#     def isPalindrome(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         rev_head = self.reverseList(head)
#         while head:
#             if head.val != rev_head.val:
#                 return False
#             head = head.next
#             rev_head = rev_head.next
#         return True
#
#     def reverseList(self, head):
#         cur, pre = head, None
#         while cur:
#             temp = cur.next
#             cur.next = pre
#             pre, cur = cur, temp
#         return pre
#
#
# test = Solution()
# node1 = ListNode(1)
# node2 = ListNode(1)
# node3 = ListNode(2)
# node4 = ListNode(1)
# node1.next = node2
# node2.next = node3
# node3.next = node4
#
# print(test.isPalindrome(node1))

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        l = len(nums)
        index = l - 1
        while index > 0:
            if nums[index - 1] < nums[index]:
                break
            index -= 1

        if index == 0:
            nums.sort()
        else:
            i = l - 1
            while i >= index:
                if nums[i] > nums[index - 1]:
                    break
                i -= 1
            nums[index - 1], nums[i] = nums[i], nums[index - 1]
            nums[:] = nums[:index] + sorted(nums[index:])
        return


test = Solution()
nums = [1, 3, 2]
test.nextPermutation(nums)
print(nums)
