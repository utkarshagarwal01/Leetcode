#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
# Definition for a Node.
from typing import Optional
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        oldToNew = {}

        def dfs(node: Optional[Node]):
            if node in oldToNew:
                return oldToNew[node]

            newNode = Node(node.val)
            oldToNew[node] = newNode

            for nei in node.neighbors:
                childNode = dfs(nei)
                newNode.neighbors.append(childNode)

            return newNode

        return dfs(node) if node else None
# @lc code=end

