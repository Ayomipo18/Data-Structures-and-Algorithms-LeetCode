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
        dfs(root);
        return;
    }
    
    public TreeNode dfs(TreeNode root) {
        if(root == null) return null;
        
        TreeNode left = dfs(root.left);
        TreeNode right = dfs(root.right);
        
        if(left != null) {
            left.right = root.right;
            root.right = root.left;
            root.left = null;
        }
        
        return right?? left?? root;
    }
}