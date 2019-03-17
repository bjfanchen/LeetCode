# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 平衡二叉树
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        mid = len(nums) // 2  # 根节点是有序list最中间的元素
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])  # 中间元素确定后，分别递归生成左右子树
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
