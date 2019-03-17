# Given a linked list, determine if it has a cycle in it.
# 解题思路：
# 设两个指针，分别为walker和runner, walker每次走1步，runner每次走两步，
# 假设链表无环，runner走到头二者也不会相遇
# 若链表有环，runner不会走到头，runner和walker一直往前走，总会有二者都进入环的情况
# 假设初始时runner滞后walker有n步，那么每次runner比walker多走一步，总会出现二者相遇

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        walker = runner = head
        while runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False
