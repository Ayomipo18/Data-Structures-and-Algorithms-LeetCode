public class Solution {
    public int LengthOfLongestSubstring(string s) {
        if(s.Length == 0) return 0;
        
        int maxLength = 1;
        
        for(int i = 0; i < s.Length; i++) {
            HashSet<char> hashset = new HashSet<char>();
            hashset.Add(s[i]);
            int currLength = 1;
            currLength = dfs(i+1, hashset, s, currLength);
            maxLength = Math.Max(maxLength, currLength);
        }
        
        return maxLength;
    }
    
    public int dfs(int index, HashSet<char> hashset, string s, int currLength) {
        if(index == s.Length || hashset.Contains(s[index])) {
            return currLength;
        }
        currLength++;
        hashset.Add(s[index]);
        return dfs(index+1, hashset, s, currLength);
    }
}