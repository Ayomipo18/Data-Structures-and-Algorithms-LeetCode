/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new List<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new List<Node>();
    }

    public Node(int _val, List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

public class Solution {
    public Node CloneGraph(Node node) {
        if(node == null) return node;
        var oldToNew = new Dictionary<Node, Node>();
        return dfs(oldToNew, node);
    }
    
    public Node dfs(Dictionary<Node, Node> oldToNew, Node node) {
        if(oldToNew.ContainsKey(node)) {
            return oldToNew[node];
        }
        
        var copy = new Node(node.val);
        oldToNew.Add(node, copy);
        foreach(var nei in node.neighbors) {
            copy.neighbors.Add(dfs(oldToNew, nei));
        }
        
        return copy;
    }
}