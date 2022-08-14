public class Solution {
    public bool IsBipartite(int[][] graph) {
        int length = graph.Length;
        int[] colors = new int[length];
        
        Array.Fill(colors, -1);
        
        for(int i = 0; i < length; i++) {
            if(colors[i] == -1) {
                colors[i] = 1;
                if(!dfs(i, graph, colors)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    private bool dfs(int index, int[][] graph, int[] colors) {
        int currentColor = colors[index];
        foreach(var connectingIndex in graph[index]) {
            if(colors[connectingIndex] == currentColor) {
                return false;
            }
            if(colors[connectingIndex] == -1) {
                colors[connectingIndex] = 1 - currentColor;
                if(!dfs(connectingIndex, graph, colors)) {
                    return false;
                }
            }
        }
        
        return true;
    }
}

//time - O(n^2)
//space - O(n)