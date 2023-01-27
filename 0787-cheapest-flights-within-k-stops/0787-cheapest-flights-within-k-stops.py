class Solution:
    '''
    - we would be using bfs
    - [0,0,0] -> [1,1,100] -> [3,2,700], [2,2,200]
    - i process all my cities at a paricular level and just get the cheapest
    - also, i might get the answer at level 2 but the cheapest is at level 7
    - so what do i do? use a priorityqueue to get the cheapest values first? yes
    - we want to start from our src till dst and make less than or at most k stops
    - so start at 0, then go to next city, keep track of cost to that city, also keep track of how many stop made already
    - create an adj_list to show all the cities a node city can point to. then from src, we do bfs(priority queue) till dest
    {0: [(1, 100)], 1: [(2, 100), (3, 600)], 2: [(0, 100), (3, 200)]}
    
    - I didn't use priority queue again, just normal queue
    - time - O(n+e)??
    - space - O(n+e)??
    where n is the number of nodes, e is the number of edges
    '''
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = collections.defaultdict(list)
        q = collections.deque([[0,src,0]])
        dist = [float('inf')] * n
        dist[src] = 0
        
        for flight in flights:
            src, dest, cost = flight[0], flight[1], flight[2]
            adj_list[src].append((dest, cost))
        
        while q:
            city_node = q.popleft()
            stops, city, cost = city_node[0], city_node[1], city_node[2]

            if stops > k:
                continue
                
            for child in adj_list[city]:
                next_city, next_city_cost = child
                if cost + next_city_cost < dist[next_city] and stops <= k:
                    dist[next_city] = cost + next_city_cost
                    q.append([stops + 1, next_city, cost + next_city_cost])
                    
        if dist[dst] == float('inf'):
            return -1
            
        return dist[dst]
        