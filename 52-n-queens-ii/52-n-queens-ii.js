/**
 * @param {number} n
 * @return {number}
 */
var totalNQueens = function(n) {
    const result = [];
    solve(n, 0, [], result);
    return result.length;
}

const solve = function(n, currRow, colQueenPlacement, result) {
    if(colQueenPlacement.length === n) {
        result.push(generateSolution(colQueenPlacement));
    } else {
        for(let col = 0; col < n; col++) {
            colQueenPlacement.push(col);
            if(isValid(colQueenPlacement)) {
                solve(n, currRow + 1, colQueenPlacement, result);
            }
            colQueenPlacement.pop();
        }
    }
}

const isValid = function(colQueenPlacement) {
    if(colQueenPlacement.length === 1) return true;
    const row = colQueenPlacement.length - 1;
    const col = colQueenPlacement[row];
    for(let i = 0; i < colQueenPlacement.length - 1; i++) {
        if(col === colQueenPlacement[i]) {
            return false;
        };
        if(row - i === Math.abs(col - colQueenPlacement[i])) {
            return false;
        };
    }
    return true;
}

const generateSolution = function(colQueenPlacement) {
    const solution = [];
    for(let i = 0; i < colQueenPlacement.length; i++) {
        let str = '';
        for(let j = 0; j < colQueenPlacement.length; j++) {
            if(colQueenPlacement[i] === j) {
                str += 'Q';
            } else str += '.';
        }
        solution.push(str);
    }
    return solution;
}