/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        /*
        - basically, get the height of each subtree, if at any subtree, it's unbalanced, return false;
        H is height of tree, N is length of input
        Time - O(N)
        Space - O(H)
        */
        return getHeight(root) != -1;
    }

    public int getHeight(TreeNode root){
        if (root == null) return 0;

        int leftHeight = getHeight(root.left);
        if(leftHeight == -1) return -1;

        int rightHeight = getHeight(root.right);
        if(rightHeight == -1) return -1;

        if(Math.abs(leftHeight-rightHeight) > 1) return -1;

        return Math.max(leftHeight, rightHeight) + 1;
    }
}