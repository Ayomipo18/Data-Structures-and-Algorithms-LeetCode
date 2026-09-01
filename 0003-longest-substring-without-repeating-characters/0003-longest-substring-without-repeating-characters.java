class Solution {
    public int lengthOfLongestSubstring(String s) {
        /*
        - longest unique substring
        - substring - subset of a string
        - unique - no duplicate
        - longest - we track state - length
        - how to take substring - 
        - s = "abcabcbb"
        - abca -> bca -> bcab -> cab -> cabc -> abc -> b

        - s = "pwwkew"
        - pww -> w -> wkew -> kew
        - Time - O(NxmaxLength)
        - Space - O(1)
        */

        HashSet<Character> hashSet = new HashSet<>();
        int maxLength = 0;
        int lastIndex = 0;

        for(char sVal:s.toCharArray()) {
            while(hashSet.contains(sVal)) {
                hashSet.remove(s.charAt(lastIndex));
                lastIndex++;
            }
            hashSet.add(sVal);
            maxLength = Math.max(maxLength, hashSet.size());
        }

        return maxLength;
    }
}