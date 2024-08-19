#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        result = []
        dp = {}

        def generate(left, right):
            if left > right:
                return [None]
            if (left, right) in dp:
                return dp[(left, right)]
            
            res = []
            for val in range(left, right+1):
                for leftTree in generate(left, val-1):
                    for rightTree in generate(val + 1, right):
                        root = TreeNode(val, leftTree, rightTree)
                        res.append(root)

            dp[(left, right)] = res

            return res 

        return generate(1, n)
        
        
# @lc code=end

