public class Solution {
    public IList<string> FindAndReplacePattern(string[] words, string pattern) {
        List<string> result = new List<string>();
        foreach(string word in words) {
            if(check(word, pattern)) result.Add(word);
        }
        return result;
    }
    
    public bool check(string a, string b) {
        for (int i = 0; i < a.Length; i++) {
            if (a.IndexOf(a[i]) != b.IndexOf(b[i])) return false;
        }
        return true;
    }
}