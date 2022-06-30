public class Solution {
    public IList<string> FindRepeatedDnaSequences(string s) {
        
        HashSet<string> hashset = new HashSet<string>();
        
        List<string> result = new List<string>();
        
        for(int i = 0; i <= s.Length - 10; i++) {
            string dna = s.Substring(i, 10);
            if(hashset.Contains(dna) && !result.Contains(dna)) {
                result.Add(dna);
            }
            else {
                hashset.Add(dna);
            }
        }
        
        return result;
    }
}