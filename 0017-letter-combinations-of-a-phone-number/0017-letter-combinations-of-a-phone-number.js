/**
 * @param {string} digits
 * @return {string[]}
 */
const letterCombinations = (digits) => {
    if(digits.length === 0) return [];
    
    const map = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }
    
    let result = [];
    
    const bT = function(i, s) {
        if(s.length === digits.length) {
            result.push(s);
            return;
        }
        
        for(let c of map[digits[i]]) {
            bT(i + 1, s + c);
        }
    }
    
    bT(0, '');
    return result;
};