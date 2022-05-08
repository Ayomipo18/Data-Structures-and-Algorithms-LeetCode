/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
  if (divisor === 0) return 0;
  if (dividend === 0) return 0;
  if (dividend === -2147483648 && divisor === -1) return 2147483647;

  var isPositive = true;
  if (dividend > 0 !== divisor > 0) isPositive = false;

  divisor = Math.abs(divisor);
  dividend = Math.abs(dividend);

  var count = 1,
    result = 0,
    base = divisor;

  while (dividend >= divisor) {
    count = 1;
    base = divisor;
    while (base <= (dividend >> 1)) {
      base = base << 1;
      count = count << 1;
    }
    result += count;
    dividend -= base;
  }

  if (!isPositive) result = -result;
  return result;
};

// var divide = function (dividend, divisor) {
//   let sign1 = Math.sign(dividend),
//     sign2 = Math.sign(divisor),
//     count = 0,
//     result = Math.abs(dividend);
//   divisor = Math.abs(divisor);
//   while (result >= divisor) {
//     result -= divisor;
//     count++;
//   }

//   if (sign1 === -1 && sign2 === -1) {
//     count = count;
//   } else if (sign1 === -1 || sign2 === -1) {
//     count = -count;
//   }
  
//   if(count > 2147483647) {
//      count = 2147483647
//   } else if(count < -2147483648) {
//       count = -2147483648
//   }
  
//   return count;
// };