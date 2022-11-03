class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        answer = 0
        central = False
        
        for word, count_word in count.items():
            if word[0] == word[1]:
                if count_word % 2 == 0:
                    answer += count_word
                else:
                    answer += count_word - 1
                    central = True
            elif word[0] < word[1]:
                    answer += 2 * min(count_word, count[word[1] + word[0]])
                    
        if central:
            answer += 1
        
        return 2 * answer