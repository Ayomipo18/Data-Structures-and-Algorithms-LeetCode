/**
 * @param {string} s
 * @return {string}
 */

var longestPalindrome = function (s) {
      let res = '';
      for(let i = 0; i < s.length; i++){
          // Odd - if there is only 1 char in the middle, like 'bob'
          let lOdd = i, rOdd = i;
          expandAroundCenter(lOdd, rOdd)
          //Even - 2 chars in the middle, like 'kbbk'
          let lEven = i, rEven = i + 1;
          expandAroundCenter(lEven, rEven);
      }
    // helper
      function expandAroundCenter(left, right){
        while(left >= 0 && right < s.length && s[left] === s[right]){
          let subStr = s.substring(left, right + 1);
          if(subStr.length > res.length){
            res = subStr;
          }
          left--;
          right++;
        }
      }
      return res;
};

// var longestPalindrome = function (s) {
//   for (let j = s.length - 1; j >= 0; j--) {
//     let i = 0,
//       k = j;
//     while (k < s.length) {
//       let substr = s.substring(i, k + 1);
//       if (isPalindrome(substr)) return substr;
//       i++, k++;
//     }
//   }
//   return "";
// };

// function isPalindrome(str) {
//   let l = 0,
//     r = str.length - 1;
//   while (l < r) {
//     if (str[l] !== str[r]) return false;
//     l++, r--;
//   }
//   return true;
// }

// var longestPalindrome = function(s) {
//     let max = '', str;
//     for(let i=0; i<s.length; i++) {
//         if(s.length === 1) return s;
//         for(let j=i; j<s.length; j++) {
//             str = s.substring(i, j+1);
//            if(palindrome(str)) max = (str.length > max.length) ? str : max; 
//         }
//     }
//     return max;
// };

// var palindrome = function(str) {
//     let left = 0, right = str.length-1;
//     while(left <= right) {
//         if(str[left] != str[right]) return false;
//         left++;
//         right--;
//     }
//     return true;
// }

