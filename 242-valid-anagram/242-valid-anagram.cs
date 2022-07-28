public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length) return false;
        
        var dict = new Dictionary<int, int>();
        for(int i = 0; i < s.Length; i++) {
            if(dict.ContainsKey(s[i])) dict[s[i]]++;
            else dict.Add(s[i], 1);
        }
        
        for(int i = 0; i < t.Length; i++) {
            if(dict.ContainsKey(t[i]) && dict[t[i]] > 0) dict[t[i]]--;
            else return false;
        }
        return true;
    }
}