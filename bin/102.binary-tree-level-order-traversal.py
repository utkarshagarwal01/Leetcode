#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.

from typing import *
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        Q = deque()
        result = []

        if root:
            Q.append(root)


        while Q:
            queueLen = len(Q)
            currLevel = []
            for _ in range(queueLen):
                node = Q.popleft()
                currLevel.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            result.append(currLevel)

        return result        

        
# @lc code=end

