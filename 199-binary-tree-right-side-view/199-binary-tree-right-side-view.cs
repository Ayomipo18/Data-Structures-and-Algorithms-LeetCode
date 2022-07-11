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
    public IList<int> RightSideView(TreeNode root) {
        IList<int> result = new List<int>();
        if(root == null) return result;
        dfs(root, 1, result);
        return result;
    }
    
    public void dfs(TreeNode root, int currLevel, IList<int> result) {
        if(root == null) return;
        if(result.Count < currLevel) {
            result.Add(root.val);
        }
        dfs(root.right, currLevel+1, result);
        dfs(root.left, currLevel+1, result);
    }
}