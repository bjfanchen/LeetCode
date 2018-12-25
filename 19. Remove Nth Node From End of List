"""
Given a linked list, remove the n-th node from the end of list and return its head.
Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
"""
# Solution One: 
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # index()函数用于获取node的逆序index（即最后一个node的index是1）
        def index(node):
            if not node:return 0
            i = index(node.next) + 1
            if i > n:node.next.val = node.val  # 需移除的node前的node的值统一后移，即覆盖了需移除元素的值，本质上节点并没有删除
            return i
        
        index(head)
        return head.next
        
# Solution Two:
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 双指针法
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        # fast为空，表示需移除的是第一个节点，因此直接返回head.next
        if not fast:
            return head.next
        # fast比slow快n个节点，当fast到达最后一个节点时，slow恰好是需移除的节点的前一节点，因此直接将其next指向下下节点即可
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        
 
