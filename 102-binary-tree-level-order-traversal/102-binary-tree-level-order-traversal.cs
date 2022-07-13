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
    public IList<IList<int>> LevelOrder(TreeNode root) {
        if(root == null) return new List<IList<int>>();
        var queue = new Queue<TreeNode>();
        var result = new List<IList<int>>();
        queue.Enqueue(root);
        
        while(queue.Count != 0) {
            int length = queue.Count;
            var currLevelValues = new List<int>();
            while(length > 0) {
                var node = queue.Dequeue();
                currLevelValues.Add(node.val);
                length--;
                if(node.left != null) queue.Enqueue(node.left);
                if(node.right != null) queue.Enqueue(node.right);
            }
            result.Add(currLevelValues);
        }
        
        return result;
    }
}