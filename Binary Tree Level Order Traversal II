# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, 0, res)
        return res
    
    def dfs(self, root, level, res):  # level表示root所在的层数，默认二叉树的根节点的level=0，res存二叉树遍历结果
        if root:  # root是否为空必须做判断，实际上该句也是递归的一个终止条件
            if len(res) < level + 1:  # 若该层还没有一个元素插入list，则在res中新建一个空的子list用来存放该层元素
                res.insert(0, [])
            res[-(level + 1)].append(root.val)  # 第0层元素插入到倒数一个list中，第1层元素插入到倒数第二个list，依次对应
            self.dfs(root.left, level + 1, res)  # 对左、右子节点递归调用插入list
            self.dfs(root.right, level + 1, res)
