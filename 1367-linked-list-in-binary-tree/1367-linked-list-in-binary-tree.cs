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
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    //Time - O(number of nodes * Max(height of tree, length of linkedlist))
    //Space - O(number of nodes)

    private ListNode _head;

    public bool IsSubPath(ListNode head, TreeNode root) {
        _head = head;
        ListNode currPointer = head;
        if(root == null) return false;
        return dfs(root, currPointer) || IsSubPath(currPointer, root.left) || IsSubPath(currPointer, root.right);
    }

    private bool dfs(TreeNode node, ListNode currPointer) {
        if(currPointer == null) return true;
        if(node ==  null) return false;
        if(node.val == currPointer.val) currPointer = currPointer.next;
        else return false;
        return dfs(node.left, currPointer) || dfs(node.right, currPointer);
    }
}