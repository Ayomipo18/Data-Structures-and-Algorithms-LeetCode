# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        - use bfs
        - priortize right, then left
        - if a value for that particular level has been filled, don't replace it, else, replace int in the result array
        
        where n is the number of nodes
        time - O(n)
        space - O(logn)
        '''
        result = []
        if not root:
            return result
        
        result.append(root.val)
        
        q = collections.deque()
        q.append((root, 1))
        
        while q:
            node, level = q.popleft()
            
            if node.right:
                q.append((node.right, level+1))
                if len(result) < level+1:
                    result.append(node.right.val)
                
            if node.left:
                q.append((node.left, level+1))
                if len(result) < level+1:
                    result.append(node.left.val)
                    
        return result