#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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

    #using Queue
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     result = []
    #     queue = deque()

    #     if root:
    #         queue.append(root)
    #         # result.append(root.val)

    #     while queue:
    #         result.append(queue[-1].val)
    #         currentLevel = []
    #         queueLen = len(queue)
    #         for _ in range(queueLen):
    #             curr = queue.popleft()
    #             if curr.left:
    #                 queue.append(curr.left)
    #             if curr.right:
    #                 queue.append(curr.right)
        
    #     return result

    #using Simpler dfs

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, level):
            if not node:
                return
            
            if len(result) == level:
                result.append(node.val)

            dfs(node.right, level + 1) 
            dfs(node.left, level + 1)

        dfs(root, 0) 
        return result
# @lc code=end