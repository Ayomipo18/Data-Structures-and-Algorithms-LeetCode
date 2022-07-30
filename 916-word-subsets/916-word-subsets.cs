public class Solution {
    public IList<string> WordSubsets(string[] words1, string[] words2) {
        int[] m = new int[26], p = new int[26];
        for (int i = 0; i < words2.Length; i++) {
            for (int j = 0; j < words2[i].Length; j++) {
                int index = words2[i][j] - 'a';
                p[index]++;
                if (p[index] > m[index]) m[index] = p[index];
            }
            
            for (int j = 0; j < 26; j++) p[j] = 0;
        }
        
        int[] t = new int[26];
        List<string> ans = new List<string>();
        for (int i = 0; i < words1.Length; i++) {
            for (int j = 0; j < words1[i].Length; j++) t[words1[i][j] - 'a']++;
            
            bool isUniversal = true;
            for (int j = 0; j < 26; j++) {
                if (m[j] > t[j]) isUniversal = false;
                t[j] = 0;
            }
            
            if (isUniversal) ans.Add(words1[i]);
        }
        
        return ans;
    }
}