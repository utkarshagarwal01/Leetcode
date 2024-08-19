#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftHeight, rightHeight = 0, 0
        leftP, rightP = root, root
        while leftP is not None:
            leftP = leftP.left
            leftHeight +=1


        while rightP is not None:
            rightP = rightP.right
            rightHeight += 1

        if leftHeight == rightHeight:
            # print("Full ", root.val, ": ", (1<<leftHeight) - 1)
            return (1<<leftHeight) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
# @lc code=end

