/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
const isMatch = (s, p) => {
	let dp = new Array(s.length + 1).fill(0).map(() => new Array(p.length + 1).fill(false));

	dp[0][0] = true;

	// fill first row
	for (let i = 1; i <= p.length; i++) {
		let pChar = p[i - 1];

		if (pChar === '*') dp[0][i] = dp[0][i - 2];
	}
	// can only be the most previous value
	for (let row = 1; row <= s.length; row++) {
		for (let col = 1; col <= p.length; col++) {
			let pChar = p[col - 1],
				sChar = s[row - 1],
				previousPChar = p[col - 2]; // col - 2 is for deletion of the previous character

			if (pChar === '*') {
				// dp[row][col - 2] --> if we shaved off the letter, would we have a match
				if (dp[row][col - 2]) {
					dp[row][col] = true;
				}
				// if previous p and sChar are the same, we look
				else if (previousPChar === sChar || previousPChar === '.') {
					// This is the weirdest case to understand
					// Since the previousPChar and sChar are equal, we can look at s as if it
					// does not exist, to account for shavng it off / extra occurances
					// of that single letter
					dp[row][col] = dp[row - 1][col];
				}
			} else if (pChar === sChar || pChar === '.') {
				// answer is the same as if not having these two letters
				dp[row][col] = dp[row - 1][col - 1];
			}
		}
	}
	return dp[s.length][p.length];
};