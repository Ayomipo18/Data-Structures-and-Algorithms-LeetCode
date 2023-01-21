public class Solution {
    //time - O(n^2)
    //space - O(1)
    public string LongestPalindrome(string s) {
        int left = 0;
        int maxLength = 0;

        for(int i = 0; i< s.Length; i++) {
            int oddStringLength = isPalindrome(i, i, s);
            int evenStringLength = isPalindrome(i, i+1, s);
            int tmpMaxLength = Math.Max(oddStringLength, evenStringLength);
            if(tmpMaxLength > maxLength) {
                left = i - ((tmpMaxLength - 1) / 2);
                maxLength = tmpMaxLength;
            }
        }

        return s.Substring(left, maxLength);
    }

    private int isPalindrome(int start, int end, string s) {
        while(start >= 0 && end < s.Length && s[start] == s[end]) {
            start--;
            end++;
        }
 
        return end - start - 1;
    }
}