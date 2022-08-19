public class Solution {
    //Time - O((numCourses + prerequisites) i.e O(V+E) worst case
    //Space - O(numCourses + prerequisites) i.e O(V+E) worst case
    private List<IList<int>> graph = new List<IList<int>>();
    private HashSet<int> cycle = new HashSet<int>();
    private HashSet<int> visited = new HashSet<int>();
    private List<int> result = new List<int>();
    
    public int[] FindOrder(int numCourses, int[][] prerequisites) {
        numCourses = numCourses;
        for(int course = 0; course < numCourses; course++) {
            graph.Add(new List<int>());
        }
        
        foreach(int[] prerequisite in prerequisites) {
            graph[prerequisite[0]].Add(prerequisite[1]);
        }

        for(int course = 0; course < numCourses; course++) {
            if(!dfs(course)) return new int[0];
        }
        
        return result.ToArray();
    }
    
    private bool dfs(int course) {
        if(cycle.Contains(course)) return false;
        if(visited.Contains(course)) return true;
        
        cycle.Add(course);
        
        foreach(int pre in graph[course]) {
            if(!dfs(pre)) return false;
        }
        
        visited.Add(course);
        result.Add(course);
        cycle.Remove(course);
        
        return true;
    }
}

//USING VISITED AS THE BASE CASE
//[[0,1], [1,2], [0,2], [0,3], [2,4]]
//create a graph {0: [1,2,3], 2: [4], 3: [], 4:[]}
//create two hashsets visited and cycle
//create a output array
//for(int i = 0; i < numCourses; i++)
//if dfs(i) == false return new int[0]
//return result

//dfs(course) returns a bool
//if(cycle.Contains(course)) return false
//if(visited.Contains(course)) return true;
//cycle.Add(course)
//for(int preReq in graph[course])
//if(!dfs(preReq)) return false;
//end of forloop
//visited.Add(course)
//output.Add(course)
//cycle.Remove(course)
//return true



//USING COUNT AS THE BASE CASE
//[[0,1], [1,2], [0,2], [0,3], [2,4]]
//create a graph {0: [1,2,3], 2: [4], 3: [], 4:[]}
//create two hashsets visited and cycle
//create a output array
//for(int i = 0; i < numCourses; i++)
//if dfs(i) == false return new int[0]
//if visited.Contains(i) continue
// visited.Add(i)
// output.Add(i)
//return result

//dfs(course) returns a bool
//if(cycle.Contains(course)) return false
//if(graph[course].Count == 0) return true;
//cycle.Add(course)
//for(int preReq in graph[course])
//if(!dfs(preReq)) return false;
//if(visited.Contains(preReq))continue
//visited.Add(preReq)
//output.Add(preReq)
//end of forloop
//cycle.Remove(course)
//graph[course] = new List<int>()
//return true