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
    public IList<IList<int>> PathSum(TreeNode root, int targetSum) {
        IList<IList<int>> result = new List<IList<int>>();
        FindPathSum(root, targetSum, new List<int>(), result);
        return result;
    }
    
    void FindPathSum(TreeNode root, int targetSum, List<int> solution, IList<IList<int>> result) {
        if (root == null) {
            return;
        }
        
        solution.Add(root.val);
        
        if(root.left == null && root.right == null && targetSum == root.val) {
            result.Add(new List<int>(solution));
        } else {
            FindPathSum(root.left, targetSum - root.val, solution, result);
            FindPathSum(root.right, targetSum - root.val, solution, result);
        }
        
        solution.RemoveAt(solution.Count - 1);
    }
}