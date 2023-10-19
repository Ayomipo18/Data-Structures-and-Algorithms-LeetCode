# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        '''
        where n is the number of nodes
        Time - O(n)
        space - O(logn)
        '''
        
        if not root:
            return 0
        left = root
        right = root
        l_h = 0
        r_h = 0
        
        while left:
            left = left.left
            l_h += 1
            
        while right:
            right = right.right
            r_h += 1
            
        if l_h == r_h:
            return int(math.pow(2, l_h)) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)