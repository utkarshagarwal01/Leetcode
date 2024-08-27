#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        count = 0
        power = 1
        while num:
            digit = num % 2
            if digit == 0:
                count += power
            power *= 2
            num //= 2

        return count
# @lc code=end

