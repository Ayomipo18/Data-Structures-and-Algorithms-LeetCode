/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000};
    let num = 0;
    for(i=0; i<s.length; i++){
        let curr = map[s[i]], next = map[s[i+1]];
        if(curr < next) num -= curr;
        else num += curr;
    }
    return num;
    
};