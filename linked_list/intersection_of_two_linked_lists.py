# Write a program to find the node at which the intersection of two singly linked lists begins.
"""
Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        pa = headA
        pb = headB
        # if either pointer hits the end, switch head and continue the second traversal, 
        # if not hit the end, just move on to next
        while pa is not pb:
            if pa:
                pa = pa.next
            else:
                pa = headB
            
            if pb:
                pb = pb.next
            else:
                pb = headA
                
        return pa 
        # only 2 ways to get out of the loop, they meet or the both hit the end=None

# the idea is if you switch head, the possible difference between length would be countered. 
# On the second traversal, they either hit or miss. 
# if they meet, pa or pb would be the node we are looking for, 
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
