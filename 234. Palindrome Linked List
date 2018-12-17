# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 首先澄清：将原链表全部反转再比较的方案不可行！
# 原因：反转链表之后，原链表的头结点head指向None，原来链表的结构也会改变且无法恢复，无法进行后续比较！！！
# Solution 1(use stack/list): 
# 利用栈（或python里的list）的“后进先出”的属性，先通过“双指针法”找到链表中点，将前半部分节点的数值存入list,
# 对后半部分进行遍历，依次将节点值与list.pop()的值比较即可
# 注意：1、链表为空或只有一个节点必回文成立，直接返回true  
# 2、以faster.next和faster.next.next均不为空作为找中点的循环条件时，考虑到链表只有两个节点的情况，因此一开始就将头结点值压栈
# 3、链表节点数为奇数时，中间节点无需参与值比较，但找中点时将其也已压栈，因此通过head.next为空的条件，将最后一个值弹出

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None: return True
        faster = slower = head
        pre_half = [head.val]
        while faster.next and faster.next.next:
            faster = faster.next.next
            slower = slower.next
            pre_half.append(slower.val)
        if not faster.next: pre_half.pop()
        
        temp = slower.next
        while temp:
            if temp.val != pre_half.pop(): return False
            temp = temp.next
        
        return True
        
# Solution 2(空间复杂度为O(1)):
# 与solution1的区别在于没有用stack另外存值，而是找到中点后，将后半部分反转，再比较
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None: return True
        faster = slower = head
        while faster.next and faster.next.next:
            faster = faster.next.next
            slower = slower.next
        new_head = self.reverseList(slower.next)
        while new_head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next
        return True
        
    def reverseList(self, head):
        cur, pre = head, None
        while cur:
            temp = cur.next
            cur.next = pre
            pre, cur = cur, temp
        return pre
