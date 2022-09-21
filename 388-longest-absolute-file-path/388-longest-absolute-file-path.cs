public class Solution {
    //time - O(n * l)
    //space - O(l) where n = number of dir&files or lines, l = max level of depth
    public int LengthLongestPath(string input) {
        Stack<int> stack = new();
        stack.Push(0); //[0, 4, 12, 22]
        int maxLength = 0;
        
        //["dir", "\tsubdir1", "\tsubdir2", "\t\tfile.ext"]
        foreach(string s in input.Split("\n")) {
            int level = s.LastIndexOf("\t") + 1; //0 1 1 2
            while(level < stack.Count - 1) {
                stack.Pop();
            }
            //0 + (3-0) + 1 = 4
            //4 + (8-1) + 1 = 12
            //4 + (8-1) + 1 = 12
            //12 + (10-1) + 1 = 22
            int len = stack.Peek() + (s.Length - level) + 1;
            //Console.WriteLine(len);
            stack.Push(len);
            if(s.Contains(".")) {
                maxLength = Math.Max(maxLength, len-1);
            }
        }
        
        return maxLength;
    }
}