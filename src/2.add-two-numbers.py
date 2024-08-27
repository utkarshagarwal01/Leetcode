#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = current = ListNode(0)
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            sum = v1 + v2 + carry
            carry = 1 if sum > 9 else 0
            sum -= 10 if sum > 9 else 0

            current.next = ListNode(sum)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next
# @lc code=end

