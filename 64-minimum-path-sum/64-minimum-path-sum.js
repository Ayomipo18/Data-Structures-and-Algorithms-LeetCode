/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    const row = grid.length;
    const col = grid[0].length;
    const dp = new Array(row).fill(0).map(() => new Array(col).fill(0));
    
    for(let i = 0; i<row; i++) {
        for(let j = 0; j<col; j++) {
            if(i===0 && j===0) {
                continue;
            }
            if (i-1 < 0) grid[i][j] += grid[i][j-1];
            else if (j-1 < 0) grid[i][j] += grid[i-1][j];
            else {
                grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1]);
            }
        }
    }
    return grid[row-1][col-1];
};