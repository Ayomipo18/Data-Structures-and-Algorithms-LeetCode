public class Solution {
    //Time - O(n * result.Length)
    //Space - O(result.Length)
    public string CountAndSay(int n) {
        string result = "1";

        for(int i = 1; i < n; i++) { //O(n)
            string currResult = generateString(result); //time/Space - //O(result.Length)
            result = currResult;
        }

        return result;
    }

    private string generateString(string value) {
        int count = 1;
        string output = "";
        for(int i = 0; i < value.Length; i++) {
            if(i+1 < value.Length && value[i] == value[i+1]) count++;
            else {
                output += count.ToString() + value[i];
                count = 1;
            }
        }
        return output;
    }
}