/**
 * @param {number} n
 * @return {number}
 */

var getMaximumGenerated = function(n) {
    if(n < 2) return n

    let array = [0, 1]
    let max = 0

    for(let i = 2; i <= n; i++) {
      if(i % 2 === 0) {
        array[i] = array[i / 2]
      } else {
        array[i] = array[(i - 1) / 2] + array[(i - 1) / 2 + 1]
      }

      if(array[i] > max) {
        max = array[i]
      }
    }

    return max
};