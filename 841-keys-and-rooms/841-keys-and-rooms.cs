public class Solution {
    private HashSet<int> hashset = new();
    
    public bool CanVisitAllRooms(IList<IList<int>> rooms) {
        dfs(0, rooms);
        if(hashset.Count == rooms.Count) return true;
        return false;
    }
    
    private void dfs(int node, IList<IList<int>> rooms) {
        if(hashset.Contains(node)) return;
        hashset.Add(node);
        if(rooms[node].Count == 0) return;
        foreach(var neighbour in rooms[node]) {
            dfs(neighbour, rooms);
        }
    }
}

/*
hashset = [0, 1, 3]
//dfs(0, rooms)

//dfs(0, rooms)
//doesn't contain
return

//dfs(1, rooms)
//doesn't contain
return

//dfs(2, rooms)
//doesn't contain
return

//dfs(3, rooms)
//doesn't contain
//return

//
*/

/*
//start at room 0
//take key 1
//at room 1, take key 2
//at room 2, take 3
//at room 3, nothing
//i have reached room 0 -> 1 -> 2 -> 3

//visited = [0,1,3]
//start at room 0, take key 1 -> take key 3(visited)
//go to room 1, take key 3 -> take key 0(visited) -> take key 1(visited)
//go to room 3, take key 0 (visited already, continue)
//go to room 3, no(visited already)
//so we didnt visit 2

//visited set = []
//dfs(0)
if(set.Count == rooms.Length) return true;
return false

//dfs function
//dfs(node) {
if(set.Contains(node)) return;
}
*/