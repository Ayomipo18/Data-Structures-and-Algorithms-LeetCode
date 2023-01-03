public class Solution {
    public int RomanToInt(string s) {
        Dictionary<char, int> dict = new(){{'I', 1}, {'V',5}, {'X',10}, {'L',50}, {'C',100}, {'D',500}, {'M',1000}};
        
        int prev = dict[s[0]];
        int result = dict[s[0]];

        for(int i = 1; i < s.Length; i++) {
            char val = s[i];
            int num_val = dict[val];
            if (prev < num_val) {
                result -= prev;
                num_val -= prev;
            }
    
            result += num_val;
            prev = dict[val];

        }
        return result;
    }
}

/*
- loop thru the string
- switch statment for different roman numerals
- sometimes addition, sometimes subtraction 
*/