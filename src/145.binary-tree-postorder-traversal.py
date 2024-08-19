#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)
            postorder.append(node.val)

        dfs(root)

        return postorder
# @lc code=end

