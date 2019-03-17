"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
解题思路：双指针！！！
采用“双指针” 的方法，一个步长1，一个步长2，当快的那个走到头时，慢的那个正好走到中间~
"""
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
        # 退出循环有两种可能：fast为空或fast.next为空，分别对应总长度为偶数和奇数的情况
        return slow
   
