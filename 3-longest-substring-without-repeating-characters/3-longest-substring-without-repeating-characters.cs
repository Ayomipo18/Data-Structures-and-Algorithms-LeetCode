public class Solution {
    public int LengthOfLongestSubstring(string s) {
        if(s.Length == 0) return 0;
        
        int maxLength = 1;
        
        for(int i = 0; i < s.Length; i++) {
            HashSet<char> hashset = new HashSet<char>();
            hashset.Add(s[i]);
            maxLength = Math.Max(maxLength, dfs(i+1, hashset, s));
        }
        
        return maxLength;
    }
    
    public int dfs(int index, HashSet<char> hashset, string s) {
        if(index == s.Length || hashset.Contains(s[index])) {
            return hashset.Count;
        }
        hashset.Add(s[index]);
        return dfs(index+1, hashset, s);
    }
}