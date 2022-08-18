public class Solution {
    //Time - O((numCourses + prerequisites) i.e O(V+E) worst case
    //Space - O(numCourses + prerequisites) i.e O(V+E) worst case
    private List<IList<int>> graph = new List<IList<int>>();
    private HashSet<int> hashSet = new HashSet<int>();
    
    public bool CanFinish(int numCourses, int[][] prerequisites) {
        for(int course = 0; course < numCourses; course++) {
            graph.Add(new List<int>());
        }
        
        foreach(int[] prerequisite in prerequisites) {
            graph[prerequisite[0]].Add(prerequisite[1]);
        }

        for(int course = 0; course < numCourses; course++) {
            if(!dfs(course)) return false;
        }
        
        return true;
    }
    
    private bool dfs(int course) {
        if(hashSet.Contains(course)) return false;
        if(graph[course].Count == 0) return true;
        
        hashSet.Add(course);
        
        foreach(int pre in graph[course]) {
            if(!dfs(pre)) return false;
        }
        
        hashSet.Remove(course);
        graph[course] = new List<int>();
        
        return true;
    }
}

    //[[0,1],[0,2],[0,3],[1,3],[2,4]]
    //[[0,1], [1,2], [2,0]]
    //create an adjacency list
    //hashset = []
    //for(int course = 0; course < numCourses; course++)
    //if(!dfs(course, hashset)) return false
    //dfs(course, hashset)
    //if(hashset.Contains(course)) return false
    //if(adjList[course].Count == 0) return true
    //foreach(node in adjList[course])
    //hashset.Add(course)
    //if(!dfs(node, hashset)) return false
    //hashset.Remove(course)
    //adjList[course] = []

//[[0,1],[0,2],[0,3],[1,3],[2,4]]
//adjList = {0: [1,2,3], 1: [], 2: [], 3: [], 4: []}
//hashset = []
//          1           1<5                 2
//for(int course = 0; course < numCourses; course++)
//dfs(0, []) true
//dfs(1, []) true
//     dfs(1, []) 
//if(!dfs(course, hashset)) return false
//return true
//dfs(0, [])
//adjList[0].Count == 3
//          2       [1,2,3]
//foreach(node in adjList[0])
//hashset = [0]
//dfs(1, [0]) true
//dfs(2, [0]) true
//dfs(3, [0]) true
//hashset = []
//adjList[0] = []
//true

//dfs(1, [])
//hashset = []
//adjList[1] = 0 true

//0->1
//dfs(1, [0])
//adjList[1].Count == 1
//          3       [3]
//foreach(node in adjList[1])
//hashset[0,1]
//dfs(3, [0,1]) true
//[0]
//adjList[1] = []
//true

//1->3
//dfs(3, [0,1])
//adjList[3].Count == 0 true

//0->2
//dfs(2, [0])
//adjList[2].Count == 1
//          4       [4]
//foreach(node in adjList[2])
//hashset = [0, 2]
//dfs(4, [0,2]) true
//hashset = [0]
//adjList[2] = []

// 2 -> 4
//dfs(4, [0,2])
//adjList[4].Count == 0 true

//0->3
//dfs(3, [0])
//adjList[3].Count == 0 true

//[[0,1], [1,2], [2,0]]
//adjList = {0: [1], 1: [2], 2: [0]}
//hashset = []
//          0            0 < 2              1
//for(int course = 0; course < numCourses; course++)
//dfs(0, []) true
//     dfs(0, []) false return false
//if(!dfs(course, hashset)) return false
//dfs(0, [])
//adjList[0].Count == 1
//          1       [1]
//foreach(node in adjList[0])
//hashset = [0]
//dfs(1, [0]) false return false
//

//0->1
//dfs(1, [0])
//adjList[1].Count == 1
//          2       [2]
//foreach(node in adjList[1])
//hashset[0,1]
//dfs(2, [0,1]) false return false

//1->2
//dfs(2, [0,1])
//adjList[2].Count == 1
//          0      [0]
//foreach(node in adjList[1])
//hashset[0,1,2]
//dfs(0, [0,1,2]) false return false

//2->0
//dfs(0, [0,1,2])
//hashset.Contains(0) return false

//2
//[[0,0],[1,1]]
//adjList = {0: [0], 1: [1]}
//dfs(0) false

//dfs(0)
//hashset = []
//adjList[0].Count = 1
//hashset = [0]
//          0      [0]
//foreach(node in adjList[0])
//dfs(0) false

//0->0
//dfs(0)
//hashset = [0] false