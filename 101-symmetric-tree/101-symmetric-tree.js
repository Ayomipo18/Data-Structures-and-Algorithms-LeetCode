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
var isSymmetric = function(root) {
    if(!root) return true;
    let queue = [root, root];
    
    while(queue.length > 0) {
        let currNode1 = queue.shift(), currNode2 = queue.shift();
        if (!currNode1 && !currNode2) continue;
        if (!currNode1 || !currNode2) return false;
        if (currNode1.val != currNode2.val) return false;
        queue.push(currNode1.left, currNode2.right);
        queue.push(currNode1.right, currNode2.left);
    }
    return true;
};
