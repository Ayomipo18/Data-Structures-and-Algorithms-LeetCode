# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    - represent your tree as a graph
    - do bfs on your graph starting from startValue till destValue
    - when you get to destValue, return string so far
    - time - O(number of nodes)
    - space - O(number of nodes)
    '''
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        adj_list = defaultdict(list)
        q = collections.deque([root])
        
        while q:
            node = q.popleft()
            
            if node.left:
                adj_list[node.left.val].append((node.val, 'U'))
                adj_list[node.val].append((node.left.val, 'L'))
                q.append(node.left)
                
            if node.right:
                adj_list[node.right.val].append((node.val, 'U'))
                adj_list[node.val].append((node.right.val, 'R'))
                q.append(node.right)
                
        
        q, node_set = collections.deque([(startValue, '')]), set()
        while q:
            node, path = q.popleft()
            node_set.add(node)
            
            for child in adj_list[node]:
                child_val, child_path = child
                if child_val in node_set:
                    continue
                if child_val == destValue:
                    return path + child_path
                q.append((child_val, path + child_path))
                
        return ''
        
        
        