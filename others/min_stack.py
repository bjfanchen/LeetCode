# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# 一句话说明题目：设计一个支持push、pop、top、min的栈，而且要在定长时间里获取到最小元素
# 解题思路：
# 栈的元素设定为tuple，tuple里包含当前元素和当前最小元素，每次push时比较当前元素和之前的最小元素，从而更新最小值

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.stack:
            self.stack.append((x, min(x, self.stack[-1][1])))
        else:
            self.stack.append((x, x))
          
    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]
