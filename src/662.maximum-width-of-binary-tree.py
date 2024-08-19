#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque()

        q.append((root, 1))

        while q:
            qLen = len(q)
            res = max(res, q[-1][1] - q[0][1] + 1)

            for _ in range(qLen):
                node, number = q.popleft()

                if node.left:
                    q.append((node.left, number*2))

                if node.right:
                    q.append((node.right, number*2 + 1))

        return res

# @lc code=end

