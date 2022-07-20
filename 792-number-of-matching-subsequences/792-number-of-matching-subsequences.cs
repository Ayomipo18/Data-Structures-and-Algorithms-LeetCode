public class Solution {
    public bool IsSubsequence(string str, string word) {
        if (string.IsNullOrEmpty(str) || string.IsNullOrEmpty(word))
            return false;
        
        int t = 0;
        for (int i = 0; i < str.Length; i++) {
            if (t == word.Length)
                return true;
            
            if (str[i] == word[t])
                t++;
        }
        
        if (t == word.Length)
            return true;
        
        return false;
    }
    
    public int NumMatchingSubseq(string s, string[] words) {
        int result = 0;
        Dictionary<string, int> wordToCount = new Dictionary<string, int>();
        
        foreach (string word in words) {
            if (wordToCount.ContainsKey(word))
                wordToCount[word]++;
            else
                wordToCount.Add(word, 1);
        }
        
        foreach (string word in wordToCount.Keys) {
            if (IsSubsequence(s, word))
                result += wordToCount[word];
        }
        
        return result;
    }
}