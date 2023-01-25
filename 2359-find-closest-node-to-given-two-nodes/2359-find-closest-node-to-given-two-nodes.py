class Solution:
    '''
    - so since we want to node1 and node2 to reach each other, so we can just pick all the values that node1 can reach and values that node2 can reach
    - if we find two values that both of them can reach, we get to the final answer
    {0: 2, 1: 2, 2: 3, 3: -1}
    {2: 1, 3: 1, -1: 2}
    - time - O(n)
    - space - O(n)
    where n is the length of edges array
    '''
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        self.adj_list = defaultdict(list)
        node1_adj, node2_adj = defaultdict(int), defaultdict(int)
        for i, edge in enumerate(edges):
            self.adj_list[i].append(edge)
            
        self.bfs(node1, node1_adj)
        self.bfs(node2, node2_adj)
        
        res, res_dist = -1, float('inf')
        
        for i in range(len(edges)):
            if i in node1_adj and i in node2_adj:
                cur_dist = max(node1_adj[i], node2_adj[i])
                if cur_dist < res_dist:
                    res = i
                    res_dist = cur_dist
                    
        return res
        
    def bfs(self, node, node_dict):
        q = collections.deque()
        q.append([node, 0])
        node_dict[node] = 0
        
        while q:
            cur_node, dist = q.popleft()
            for child in self.adj_list[cur_node]:
                if child not in node_dict:
                    q.append([child, dist + 1])
                    node_dict[child] = dist + 1
                
        
        