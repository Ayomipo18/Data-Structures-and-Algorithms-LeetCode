/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
  const result = [];

  const go = (l, r, s) => {
    if (l > r) return;

    if (l === 0 && r === 0) {
      result.push(s);
      return;
    }

    if (l > 0) go(l - 1, r, s + '(');
    if (r > 0) go(l, r - 1, s + ')');
  };

  go(n, n, '');
  return result;
};