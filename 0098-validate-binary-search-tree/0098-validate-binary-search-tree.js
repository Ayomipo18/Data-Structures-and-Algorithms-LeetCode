/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
    if(!root) return true;
    return dfs(root, -Infinity, Infinity);
}

var dfs = function(node, min, max) {
    if(node.val <= min || node.val >= max) {
        return false;
    }
    
    if(node.left) {
        if(!dfs(node.left, min, node.val)) {
            console.log(min)
            return false;
        }
    }
    
    if(node.right) {
        if(!dfs(node.right, node.val, max)) {
            return false;
        }
    }
    
    return true;
}