/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode ReverseBetween(ListNode head, int left, int right) {
        int currPos = 1;
        ListNode start = head;
        ListNode currNode = head;
        
        while(currPos<left) {
            start = currNode;
            currNode = currNode.next;
            currPos++;
        }
    
        ListNode tempNext;
        ListNode newList = null;
        ListNode tail = currNode;
        
        while(currPos>=left && currPos<=right) {
            tempNext = currNode.next;
            currNode.next = newList;
            newList = currNode;
            currNode = tempNext;
            currPos++;
    }
        
        start.next = newList;
        tail.next = currNode;
        if(left>1) return head;
        else return newList;
            
    }
}