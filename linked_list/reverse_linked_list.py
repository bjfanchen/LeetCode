"""
链表反转
非递归法：（迭代法）
设两个指针，分别指向当前节点和上一节点，每次只改变当前节点的指向，将其next指向其上一节点，依次迭代进行即可，循环条件是当前节点不为空
"""


class Solution(object):
    def reverseList(self, head):
        cur, pre = head, None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur =temp
        return pre

"""
递归法：
核心思想：假设当前节点为ak，其之后的节点已经实现了链表反转，那么如何实现ak+1指向ak的反转？
ak.next.next = ak
ak.next = None（必须！保证链表单向不会形成环的必要步骤~）
基线条件：
1、head.next为空，表明是链表的最后一个节点，返回head作为反转后的头结点
2、head为空，链表为空，直接返回head
二者可以合并~
"""

# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head == None or head.next == None: return head
#         p = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return p

# sol = Solution()
# print(sol.reverseLise())

