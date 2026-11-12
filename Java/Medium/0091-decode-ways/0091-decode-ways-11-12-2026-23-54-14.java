class Solution {
    public int numDecodings(String s) {
        		// your code goes here
		/*
        time - O(n)
        Space - O(n)
        n - length of string s
		- state = length of s
		- base case dp[0] = 1
		- number of ways - addition
		- formular - dp[i-1] if it's valid
		or dp[i-2] if it's valid
		*/
		int n = s.length();
		int[] dp = new int[n+1];
		dp[0] = 1;

		for(int i=1; i<=n; i++) {
			if(s.charAt(i-1) != '0') dp[i] += dp[i-1];
			if(i>=2) {
				int two = Integer.parseInt(s.substring(i-2, i));
				if(two >= 10 && two <= 26) dp[i] += dp[i-2];
			}
		}

		return dp[n];
    }
}