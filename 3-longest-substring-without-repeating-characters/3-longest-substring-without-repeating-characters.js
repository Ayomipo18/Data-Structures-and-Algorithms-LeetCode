/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(string) {
    if(string.length<=1) return string.length;
    let left = 0, longest=0;
    const seenChars = {};
    
    for(let right = 0; right<string.length; right++){
        let currentChar = string[right];
        let previouslySeenChar = seenChars[currentChar];
        if(previouslySeenChar >= left) {
            left = previouslySeenChar + 1;
        }
        
        seenChars[currentChar] = right;
        longest = Math.max(longest, right-left+1)
    }
    
    return longest;
};