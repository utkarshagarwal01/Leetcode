#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ["{", "(", "["]:
                stack.append(char)
            else:
                inStack = stack[-1] if stack else ""
                if (char == "}" and inStack == "{") or \
                    (char == "]" and inStack == "[") or \
                    (char == ")" and inStack == "("):
                    stack.pop()
                else:
                    return False
                
        return not len(stack)
        
# @lc code=end

