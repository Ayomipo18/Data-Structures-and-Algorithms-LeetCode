# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # p_set = []
    # q_set = []
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        where n is the number of nodes
        
        solution 2
        time - O(logn)
        space - O(logn)
        '''
        
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        else:
            return left or right
    
#         tree_set = []
        
#         self.dfs(root, tree_set, p, q)
        
#         for i in range(len(Solution.p_set)-1, -1, -1):
#             for j in range(len(Solution.q_set)-1, -1, -1):
#                 if Solution.p_set[i] == Solution.q_set[j]:
#                     return Solution.p_set[i]
            
#         return 0
    
#     def dfs(self, node, node_set, p, q):
#         node_set.append(node)
        
#         if node.val == p.val:
#             Solution.p_set = node_set.copy() 
#         elif node.val == q.val:
#             Solution.q_set = node_set.copy()
        
#         if node.left:
#             self.dfs(node.left, node_set.copy(), p, q)
            
#         if node.right:
#             self.dfs(node.right, node_set.copy(), p, q)