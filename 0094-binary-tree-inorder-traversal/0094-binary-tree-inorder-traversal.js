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
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    const values = [];
    if(!root) return values;
    dfs(root, values);
    return values
};

var dfs = function(node, values) {
    if(node.left) dfs(node.left, values);
    values.push(node.val);
    if(node.right) dfs(node.right, values);
    return;
};