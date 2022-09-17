public class FileSystem {
    //where n is the length of path
    //where k = number of unique paths we add
    //time - O(n)
    //space - O(k)
    Dictionary<string, int> paths;

    public FileSystem() {
        paths = new();
    }
    
    public bool CreatePath(string path, int value) {
        if(String.IsNullOrEmpty(path) || path.Equals("/") || paths.ContainsKey(path)) {
            return false;
        }
        
        int delimeter = path.LastIndexOf("/"); //O(n)
        string parent = path.Substring(0, delimeter); //O(n)
        
        if(parent != String.Empty && !paths.ContainsKey(parent)) {
            return false;
        }
        
        paths.Add(path, value);
        return true;
    }
    
    public int Get(string path) {
        if(paths.ContainsKey(path)) {
            return paths[path];
        } else {
            return -1;
        }
    }
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem obj = new FileSystem();
 * bool param_1 = obj.CreatePath(path,value);
 * int param_2 = obj.Get(path);
 */

//we would use a paths = dictionary<string, int>
//initialize file system with the dictionary
//for createpath
    //if the path is empty or it just contains "/" or that path already exists, return false
    //"/leet"
    //delim = path.LastIndexOf("/")
    //parent = path.Substring(0, delim)
    //if(parent.Length > 1 && !paths.ContainsKey(parent)) return false;
    //paths.Add(path, value);
    //return true

//for getpath
    //if(paths.ContainsKey(path)) return paths[path]
    //return -1