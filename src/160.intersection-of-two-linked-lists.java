/*
 * @lc app=leetcode id=160 lang=java
 *
 * [160] Intersection of Two Linked Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public static int getLength(ListNode head) {
        int l = 0;
        while(head != null) {
            ++l;
            head = head.next;
        }
        return l;
    }
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lenA = getLength(headA), lenB = getLength(headB);
        
        ListNode longer = lenA > lenB? headA: headB;
        ListNode shorter = lenA > lenB? headB: headA;
        int diff = Math.abs(lenA - lenB);
        
        while(diff-- > 0) {
            longer = longer.next;
        }

        while(longer != null && shorter != null) {
            if (longer == shorter) {
                return longer;
            }
            longer = longer.next;
            shorter = shorter.next;
        }
        return null;
    }
}
// @lc code=end

