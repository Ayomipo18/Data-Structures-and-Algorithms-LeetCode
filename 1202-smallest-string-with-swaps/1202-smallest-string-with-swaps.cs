public class Solution {
    //Final Space complexity - O(s.Length ^ 2)
    //Final time complexity - O(Max(s.Length, pairs.Length))
    
    public string SmallestStringWithSwaps(string s, IList<IList<int>> pairs) {
        char[] charArray = s.ToCharArray(); //[d, c, a, b] space/time -  O(s.Length)
        
        Dictionary<int, PriorityQueue<char, char>> dict = new(); 
        /*
        space - O(s.Length/2 * s.Length) = O(s.Length ^ 2)
        {
        0: [[b, b], [d, d]]
        1: [[a, a], [c, c]]
        }
        */
        UnionFind uf = new UnionFind(charArray.Length); //time/space - O(s.Length)
        
        foreach(List<int> pair in pairs) { //time - O(pairs.Length)
            uf.Unify(pair[0], pair[1]); //(0,3) - (1,2) //time - 1^s.Length
        }
        
        // foreach(var value in uf.parent) {
        //     Console.WriteLine(value);
        // }
        
        //i = 0 - 1 - 2 - 3
        for(int i = 0; i < charArray.Length; i++){ // time - O(s.Length)
            int parentId = uf.GetAbsoluteParent(i); //0 - 1 - 1 - 0 //time - 1^s.Length
            if(!dict.ContainsKey(parentId)) {
                dict.Add(parentId, new PriorityQueue<char, char>());
            }
            dict[parentId].Enqueue(charArray[i], charArray[i]);
        }
        
        //i = 0 - 1 - 2 - 3
        for(int i = 0; i < charArray.Length; i++) { //time - O(s.Length)
            int parentId = uf.GetAbsoluteParent(i); //0 - 1 - 1 - 0 //time - 1^s.Length
            
            //charArray = [b, a, c, d]
            charArray[i] = dict[parentId].Dequeue();
        }
        
        return new string(charArray); // time - O(s.Length)
    }
}

public class UnionFind {
    public int[] parent; //[0, 1, 1, 0]
    
    public UnionFind(int n){
        parent = new int[n];
        for(int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    
    public int GetAbsoluteParent(int i) {
        if(parent[i] == i) {
            return i;
        }
        parent[i] = GetAbsoluteParent(parent[i]);
        return parent[i];
    }
    
    public void Unify(int i, int j) {
        int absoluteParentI = GetAbsoluteParent(i); //1
        int absoluteParentJ = GetAbsoluteParent(j); //2
        if(absoluteParentI != absoluteParentJ) {
            parent[absoluteParentJ] = absoluteParentI; //parent[2] = 1
        }
    }
}