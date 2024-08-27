#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
from bisect import bisect
class MyCalendar:

    def __init__(self):
        self.calender = []
        

    def book(self, start: int, end: int) -> bool:

        insertPos = bisect(self.calender, start, key=lambda x: x[0])
        n = len(self.calender)
        
        if 0 <= insertPos-1 and self.calender[insertPos-1][1] > start:
            return False
        
        if insertPos < n and end > self.calender[insertPos][0]:
            return False
        
        self.calender.insert(insertPos, [start, end])
        return True
            
            



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

