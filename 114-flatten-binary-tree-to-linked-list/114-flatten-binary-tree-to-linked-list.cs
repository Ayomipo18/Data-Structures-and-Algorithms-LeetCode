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
    public void Flatten(TreeNode root) {
        helper(root);
    }

    public TreeNode helper(TreeNode root) {
        if(root == null) return null;
        TreeNode leftMost = helper(root.left);
        TreeNode rightMost = helper(root.right);
        TreeNode right = root.right;
        if(leftMost != null) {
            root.right = root.left;
            leftMost.right = right;
        }
        root.left = null;
        return rightMost ?? leftMost ?? root;
    }
    //1st
    //root = 1
    //root.left = 2
    //leftmost = 4
    //2nd
    //root = 2
    //root.left = 3
    //leftmost = 3
    //rightmost = 4
    //2.right = 3;
    //3.right = 4
    // 4
    //3rd
    //root = 3
    //root.left = null
    //leftMost = null
    //rightmost = null
    //right = null
}