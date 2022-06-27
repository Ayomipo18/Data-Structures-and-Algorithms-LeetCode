public class Solution {
    public IList<int> FindSubstring(string s, string[] words) {
        if (s == string.Empty || words.Length == 0)
        {
            return new List<int>();
        }
        
        Dictionary<string, int> wordFrequency = new Dictionary<string, int> ();
        
        for(int i = 0; i < words.Length ; i++)
        {
            if(!wordFrequency.ContainsKey(words[i])) 
                wordFrequency.Add(words[i], 0);
            wordFrequency[words[i]]++;
        }
        
        int wordsCount = words.Length;
        int wordLength = words[0].Length;
        
        List<int> resultIndices = new List<int>();
        for (int i = 0; i < (s.Length - wordsCount*wordLength) + 1; i++) {
            Dictionary<string, int> wordsSeen = new Dictionary<string, int>();
            for(int j = 0; j < wordsCount; j++)
            {
                int nextWordIndex = i + j * wordLength;
                string validSubstring = s.Substring(nextWordIndex, wordLength);
                if(!wordFrequency.ContainsKey(validSubstring)) 
                    break;
                if(!wordsSeen.ContainsKey(validSubstring))
                    wordsSeen.Add(validSubstring, 0);
                wordsSeen[validSubstring]++;
                if(wordsSeen[validSubstring] > wordFrequency[validSubstring]) 
                    break;
                if(j + 1 == wordsCount)
                    resultIndices.Add(i);                
            }
        }
        return resultIndices;
    }
}