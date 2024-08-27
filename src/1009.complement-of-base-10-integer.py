#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        count = 0
        power = 1
        if not n:
            return 1
        while n:
            digit = n % 2
            if digit == 0:
                count += power
            power *= 2
            n //= 2

        return count
        
# @lc code=end

