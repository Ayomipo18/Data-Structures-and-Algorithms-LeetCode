public class Solution {
    //time - O(n) n = palindrome.length
    //space - O(n)
    public string BreakPalindrome(string palindrome) {
        if(palindrome.Length == 1) return "";
        int lastIndex = -1;
        StringBuilder sb = new(palindrome);
        for(int i = 0; i < palindrome.Length; i++) {
            if(sb[i] != 'a') {
                if(lastIndex >= 0) {
                    sb[lastIndex] = 'a';
                    return sb.ToString();
                } else {
                    lastIndex = i;
                }
            }
        }
        sb[sb.Length - 1] = 'b';
        return sb.ToString();
    }
}