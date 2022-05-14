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
 * @return {number}
 */
var minDepth = function(root, currDepth=0) {
    if(!root) return currDepth;
    currDepth++;
    if(!root.left) return minDepth(root.right, currDepth);
    if(!root.right) return minDepth(root.left, currDepth);
    return Math.min(minDepth(root.left, currDepth), minDepth(root.right, currDepth));
};