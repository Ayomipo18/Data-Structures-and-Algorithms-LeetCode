/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(letters) {
    let res = [];
    dfs(letters, [], Array(letters.length).fill(false), res);
    return res;
}

function dfs(letters, path, used, res) {
    if (path.length == letters.length) {
        res.push([...path]);
        return;
    }
    for (let i = 0; i < letters.length; i++) {
        if (used[i]) continue;
        path.push(letters[i]);
        used[i] = true;
        dfs(letters, path, used, res);
        path.pop();
        used[i] = false;
    }
}