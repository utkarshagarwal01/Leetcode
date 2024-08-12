#
# @lc app=leetcode id=542 lang=python
#
# [542] 01 Matrix
#

# @lc code=start
import collections
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        directions = [(1,0), (-1, 0), (0,-1), (0,1)]
        result = [[0] * n  for _ in range(m)]

        queue = collections.deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
                    visited.add((i,j))


        while queue:
            i, j, level = queue.popleft()
            
            result[i][j] = level

            for x, y in directions:
                idx, jdx = i + x, j + y
                if 0 <= idx < m and \
                    0 <= jdx < n and \
                    (idx, jdx) not in visited:
                    queue.append((idx, jdx, level + 1))
                    visited.add((idx, jdx))

        return result

# @lc code=end