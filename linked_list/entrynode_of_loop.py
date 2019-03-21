# -*- coding: utf-8 -*
# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Sol:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        fast = slow = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                temp = pHead
                while temp != fast:
                    temp = temp.next
                    fast = fast.next
                return temp
        return None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1
# node4.next = None

mysolution = Sol()
print(mysolution.EntryNodeOfLoop(node1).val)
