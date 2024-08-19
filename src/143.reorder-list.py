#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def printList(self, head):
        while head:
            print(head.val)
            head = head.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return head
         
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp


        first, second = head, prev
        self.printList(first)
        self.printList(second)
        

        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first, second = temp1, temp2

        return head

# @lc code=end

