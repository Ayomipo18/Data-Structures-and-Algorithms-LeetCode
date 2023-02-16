# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = collections.deque([root])
        
        max_depth = 0
        
        while q:
            max_depth += 1
            length = len(q)
            
            while length > 0:
                node = q.popleft()
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
                
                length -= 1
            
        return max_depth