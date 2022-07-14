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
    public TreeNode BuildTree(int[] preorder, int[] inorder) {
        Dictionary<int,int> inorderIdx = new Dictionary<int,int>();
		
        for(int i=0;i<inorder.Length;i++)
            inorderIdx[inorder[i]] = i;
        
		int preIdx = 0;
        return Build(0,preorder.Length-1);
		
        TreeNode Build(int inStartIdx, int inLastIdx)
        {
            if(inStartIdx>inLastIdx) return null;
            
            TreeNode root = new TreeNode(preorder[preIdx]);
            int rootIdx = inorderIdx[preorder[preIdx++]];
            root.left = Build(inStartIdx,rootIdx-1);
            root.right = Build(rootIdx+1,inLastIdx);
            return root;
        }
    }
}