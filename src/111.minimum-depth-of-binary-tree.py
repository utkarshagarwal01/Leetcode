#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        
        if leftDepth and rightDepth:
            return 1 + min(leftDepth, rightDepth)

        return 1 + (leftDepth or rightDepth)
# @lc code=end

