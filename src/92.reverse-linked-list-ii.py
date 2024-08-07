#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        dummy = ListNode(0, head) 
        leftPrev, curr = dummy, head
        c = 0

        for i in range(left-1):
            leftPrev, curr = curr, curr.next

        prev = None
        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt

 
        leftPrev.next.next = curr
        leftPrev.next = prev

        return dummy.next
# @lc code=end

