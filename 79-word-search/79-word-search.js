/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const n = board.length, m = board[0].length;
    if (word.length < 1) return false;

    const backTrack = (i, j, pos) => {
        if (i === n || i < 0 || j === m || j < 0 || board[i][j] !== word[pos]) return false;
        if (pos === word.length-1) return true;
        board[i][j] = ".";
        const found = 
            backTrack(i+1,j, pos+1) ||
            backTrack(i-1,j, pos+1) ||
            backTrack(i,j+1, pos+1) ||
            backTrack(i,j-1, pos+1);

        board[i][j] = word[pos];
        return found;
    };
    
    for (let i=0;i<n;i++) {
        for (let j=0;j<m;j++) {
            if (board[i][j] === word[0]) {
                const match = backTrack(i,j, 0);
                if (match) return true;
            }
        }
    }

    return false; 
};