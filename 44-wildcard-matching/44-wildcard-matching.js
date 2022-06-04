/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = (s, p) => {
	let dp = new Array(s.length + 1).fill(0).map(() => new Array(p.length + 1).fill(false));

    dp[0][0] = true;
    
    for (var col = 1; col <= dp[0].length; col ++) {
        if (p[col - 1] === '*') {
            dp[0][col] = dp[0][col - 1];
        }
    }

	for (let row = 1; row < dp.length; row++) {
		for (let col = 1; col < dp[0].length; col++) {
			let sLetter = s[row - 1],
				pLetter = p[col - 1];

			if (sLetter == pLetter || pLetter == '?')
				dp[row][col] = dp[row - 1][col - 1];
			else if (pLetter == '*')
				dp[row][col] = dp[row][col - 1] || dp[row - 1][col];
		}
	}

	return dp[s.length][p.length];
};