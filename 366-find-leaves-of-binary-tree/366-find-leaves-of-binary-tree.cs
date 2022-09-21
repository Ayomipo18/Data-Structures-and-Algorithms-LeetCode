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
    List<int> currLevel;
    IList<IList<int>> result = new List<IList<int>>();
    
    public IList<IList<int>> FindLeaves(TreeNode root) {
        
        while(root.left != null || root.right != null) {
            currLevel = new();
            dfs(root);
            result.Add(new List<int>(currLevel));
        }
        
        result.Add(new List<int>(){root.val});
        return result;
    }
    
    private bool dfs(TreeNode node) {
        if(node.left == null && node.right == null) {
            currLevel.Add(node.val);
            return true;
        } else {
            if(node.left != null) {
                bool left = dfs(node.left);
                if(left) node.left = null;
            }
            
            if(node.right != null) {
                bool right = dfs(node.right);
                if(right) node.right = null;
            }
        }
        return false;
    }
}

//List<List<int>> result = new();
//do dfs
    //while(node.left != null && node.right != null)
        //dfs(root, new List<int>())
    //result.Add(root.val)
//result = [4, 5, 3]
/*dfs(TreeNode node, List<int> currResult)
    if(node.left == null && node.right == null) {
        //currResult.Add(node)
        result.Add(new List<int>(currResult));
        currResult.RemoveAt(currResult.Length-1);
        node = null;
        return;
    } else {
        if(node.left != null) {
            dfs(node.left, currResult)
        }
        if(node.right != null) {
            dfs(node.right, currResult)
        }
        return;
    }
*/