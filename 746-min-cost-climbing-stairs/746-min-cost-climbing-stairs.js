/**
 * @param {number[]} cost
 * @return {number}
 */

// var minCost = function(i, cost) {
//   if(i < 0) return 0;
//   if(i === 0 || i === 1) return cost[i];
//   return cost[i] + Math.min(minCost(i - 1, cost), minCost(i - 2, cost));
// }

const minCostClimbingStairs = function(cost) {
  const n = cost.length;
  if(n === 0) return 0;
  if(n === 1) return cost[0];
  for(let i = 0; i < n; i++) {
    if (i >= 2) {
      cost[i] = cost[i] + Math.min(cost[i - 1], cost[i - 2]);
    }
  }

  return Math.min(cost[n - 1], cost[n - 2]);
};

// var minCostClimbingStairs = function(cost) {
//   const n = cost.length;
//   if(n === 0) return 0;
//   if(n === 1) return cost[0];
//   let costOne = cost[0];
//   let costTwo = cost[1];
//   for(let i = 2; i < n; i++) {
//     const current = cost[i] + Math.min(costOne, costTwo);
//     costOne = costTwo;
//     costTwo = current;
//   }

//   return Math.min(costOne, costTwo);
// };