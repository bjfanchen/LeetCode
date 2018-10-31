"""
移除链表中的指定元素（给定值，不止一个）
思路：
对链表来说，移除指定元素，改变的只有其上一个节点的next指向
因此，考虑创建一个节点作为头节点的上一节点，从头节点开始遍历，
若找到指定元素，则修改其母节点的指向，并依次向后遍历
需要注意的是：
由于要保存起始位置，在新建一个节点作为头节点的上一个节点的基础上，
还要新建一个变量指向它，从而在遍历的过程中不修改起始节点（即头节点的上一节点）~
"""
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            if val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
