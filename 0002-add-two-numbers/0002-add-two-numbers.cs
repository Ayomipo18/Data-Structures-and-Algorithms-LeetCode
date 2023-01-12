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
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode result = new ListNode();
        ListNode temp = result;
        int node1;
        int node2;
        int sum;
        
        while(l1 != null || l2 != null || carry > 0) {
            if(l1 == null) node1 = 0;
            else node1 = l1.val;
            
            if(l2 == null) node2 = 0;
            else node2 = l2.val;
            
            sum = node1 + node2 + carry;
            int nodeValue = sum % 10;
            int carryValue = sum / 10;
            
            temp.next = new ListNode(nodeValue);
            carry = carryValue;
            
            l1 = l1?.next;
            l2 = l2?.next;
            temp = temp.next;
        }
        
        return result.next;
    }
}