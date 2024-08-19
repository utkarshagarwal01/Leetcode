#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node): #[maxHeight, diameter]
            if not node:
                return [0, 0]
            
            leftH, leftD = dfs(node.left)
            rightH, rightD = dfs(node.right)

            return [1 + max(leftH, rightH), max(leftD, rightD, leftH + rightH)]
        
        return dfs(root)[1]
# @lc code=end

