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
    //Time complexity - O(n) where n is the number of nodes in the tree
    //Space complexity - O(1)
    private int count = 1;
    
    public int MaxDepth(TreeNode root) {
        if(root == null) return 0;
        dfs(root, 1);
        return count;
    }
    
    private void dfs(TreeNode node, int currCount) {
        if(node == null) return;
        if(currCount > count) count = currCount;
        dfs(node.left, currCount + 1);
        dfs(node.right, currCount + 1);
        return;
    }
}
//have a count variable
//then do dfs in preoreder style(NLR)
//dfs(node, currCount)
//if(node == null) return
//if(currCount > count) count = currCount
//dfs(node.left, currCount + 1)
//dfs(node.right, currCount + 1)
//return

//private count = 1
//MaxDepth(root)
//if(root == null) return 0;
//dfs(root, 1)
//return count;

//dfs(3, 1)
//1 > 1 no
//dfs(9, 2)
//dfs(20, 2)

//dfs(9, 2)
//2 > 1 count = 2
//dfs(null, 3) left
//dfs(null, 3) right
//return

//9.left
//dfs(null, 3)
//return

//9.right
//dfs(null, 3)
//return

//dfs(20, 2)
//2 > 2 no
//dfs(15, 3)

//dfs(15, 3)
//3 > 2 count = 3
//dfs(null, 4)
//dfs(null, 4)

//dfs(null, 4)
//return