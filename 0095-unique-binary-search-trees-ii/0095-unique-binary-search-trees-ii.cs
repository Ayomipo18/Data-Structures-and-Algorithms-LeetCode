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
    public IList<TreeNode> GenerateTrees(int n) {
            return helper(1,n);
    }
    public List<TreeNode> helper(int left, int right){
        List<TreeNode> ans = new List<TreeNode>();
        if(left>right){
            ans.Add(null);
            return ans;
        }
        if(left==right){
            ans.Add(new TreeNode(left));
            return ans;
        }
        for(int i=left; i<=right; i++){
            List<TreeNode> lft = helper(left, i-1);
            List<TreeNode> rgt = helper(i+1, right);
            
            foreach(TreeNode l in lft){
                foreach(TreeNode r in rgt){
                    ans.Add(new TreeNode(i, l ,r));
                }
            }
        }
        return ans;
    }
}