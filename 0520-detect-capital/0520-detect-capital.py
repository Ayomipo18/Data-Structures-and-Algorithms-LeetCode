class Solution:
    '''
    - if the first word is a small letter, then no other letter must be a capital letter
    - if the firstword is a capital letter and i continue counting capital letters and it gives me len of word, return True,
    keep two variables, first word and count, return true if first_word and count == 0
    true if first_word == 1 and count == 1
    true if first_word == 1 and count == len(word)

    time - O(n)
    space - O(1)
    where n is the length of word
    '''
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        n = len(word)

        first_word = 1 if word[0].isupper() else 0
        for i in range(1, n):
            count = count + 1 if word[i].isupper() else count

        count += first_word
        if (first_word == count) or (first_word == 1 and count == n):
            return True

        return False