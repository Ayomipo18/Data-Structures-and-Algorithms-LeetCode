/**
 * @param {number} n
 * @return {number}
 */

// var fib = function(n) {
//     if(n === 0) return 0;
//     if(n === 1) return 1;
//     return fib(n-1) + fib(n-2);
// }

// var fib = (n, memo = []) => {
//     if(n === 0) return 0;
//     if (n === 1 || n === 2 ) return 1;
//     if (memo[n]) return memo[n];
//     memo[n] = fib(n-1, memo) + fib(n-2, memo);
//     return memo[n];
// }

// var fib = function(n) {
//   const memo = {}
//   const helper = (x) => {
//     if(memo[x]) return memo[x]
//     if(x === 1 || x === 0) return x
//     return memo[x] = helper(x-1) + helper(x-2)
//   }
//   return helper(n);
// };

// var fib = function(n) {
//     let dp = [0, 1];
//     for(let i = 2; i <= n; i++) {
//         dp[i] = dp[i-1] + dp[i-2];
//     }
//     return dp[n];
// }

var fib = function(n) {
     let dp1 = 0, dp2 = 1, curr;
     if(n === 0) return 0;
     for(let i = 2; i <= n; i++) {
         curr = dp1 + dp2;
         dp1 = dp2;
         dp2 = curr;
     }
     return dp2;
}