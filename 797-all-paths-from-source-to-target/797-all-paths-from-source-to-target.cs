public class Solution {
    //time - O()
    IList<IList<int>> result = new List<IList<int>>();
    int length;
    
    public IList<IList<int>> AllPathsSourceTarget(int[][] graph) {
        //run a dfs on the graph starting from index 0
        //then do recursive calls on each child node in the passed node.
        //so start at index 0 in the AllPathsSourceTarget func
        //the foreach index in graph[node], do a recursive call
        //if current node/index passed is 4, push, then, return
        //if the node passed is null, don't push but return;
        length = graph.Length;
        dfs(graph, 0, new List<int>());
        return result;
    }
    
    private void dfs(int[][] graph, int node, IList<int> path) {
        if(node == null) return;
        path.Add(node);
        if(node == length-1) {
            result.Add(new List<int>(path));
            return;
        }
        
        foreach(int connectingNode in graph[node]) {
            dfs(graph, connectingNode, path);
            path.RemoveAt(path.Count - 1);
        }
        
        return;
    }
    
    //main reursive call
    //path = [0]
    //dfs(graph, 4, [0], 5)
    //dfs(graph, 3, [0], 5)
    //dfs(graph, 1, [0], 5)
    //return
    
    //1st recursive call(0 -> 4)
    //path = [0, 4]
    //result = [[0, 4]]
    //return
    
    //0 -> 3
    //path = [0, 3]
    //dfs(graph, 4, [0,3], 5)
    //return
    
    //3 -> 4
    //path[0, 3, 4]
    //result[[0,4], [0,3,4]]
    //return
    
    //0 -> 1
    //[0, 1]
    //dfs(graph, 3, [0,1], 5)
    //dfs(graph, 2, [0,1], 5)
    //dfs(graph, 4, [0,1], 5)
    //edgecase dfs(graph, null, [0,1], 5)
    //return
    
    //edge case
    // 1-> null
    //return
    
    //1 -> 3
    //[0,1,3]
    //dfs(graph, 4, [0,1,3], 5)
    
    // 3 -> 4
    //path = [0,1,3,4]
    //result[[0,4], [0,3,4], [0, 1, 3, 4]]
    //return
    
    //1->2
    //[0,1,2]
    //dfs(graph, 3, [0,1,2], 5)
    
    //2->3
    //[0,1,2,3]
    //dfs(graph, 4, [0,1,2,3], 5)
    
    // 3 -> 4
    //path = [0,1,2,3,4]
    //result[[0,4], [0,3,4], [0, 1, 3, 4], [0, 1, 2, 3, 4]]
    //return
    
    //1->4
    //path = [0,1,4]
    //result[[0,4], [0,3,4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0,1,4]]
    //return
}