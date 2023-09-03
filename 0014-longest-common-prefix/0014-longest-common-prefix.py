class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #choose an arbitrary string as ref, most ikely the first string
        #go thru the abritrary string, then pick each of the letters in each word and compare
        #if the comparism is valid, add to result, else return result
        
        res = ""
        
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
            
        return res