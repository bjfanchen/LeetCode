# 给定二叉树，找出它的最小高度
# 思路：
# 关于二叉树，还是考虑递归办法，计算最小路径具体分析有5种情形：
# 1.根节点为空 2.只有一个根节点 3.只有左子树 4.只有右子树 5.左右子树都有
# 1最简单，直接返回0
# 3和4需考虑：只有左子树，那计算路径只用计算左子树部分再加1（根节点）；只有右子树，结果相似
# 2和5情况相似，不用分开考虑左右子树，递归计算即可

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right == None:
            return self.minDepth(root.left) + 1
        if root.right and root.left == None:
            return self.minDepth(root.right) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
