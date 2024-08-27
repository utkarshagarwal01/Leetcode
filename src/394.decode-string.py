#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        accumulateNum = []
        accumulateString = []
        for char in s:
            
            isNum = ord('0') <= ord(char) <= ord('9')
            isLetter = ord('a') <= ord(char) <= ord('z')

            if isLetter:
                accumulateString.append(char)
            elif accumulateString:
                string = "".join(accumulateString)
                accumulateString = []
                stack.append(string)
                
            if isNum:
                accumulateNum.append(char)
            elif accumulateNum:
                number = "".join(accumulateNum)
                accumulateNum = []
                stack.append(number)
            
            if char == ']':
                part = ""
                while not stack[-1].isnumeric():
                    part = stack.pop() + part
                count = int(stack.pop())
                stack.append(part * count)      

        res = "".join(stack + accumulateString) 
        # print(res)
        return res


# @lc code=end

