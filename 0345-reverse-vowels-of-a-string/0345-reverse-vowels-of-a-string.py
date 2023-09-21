# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowels_map = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#         left, right = 0, len(s)-1
#         s_arr = list(s)
        
#         while left < right:
#             if s_arr[left] not in vowels_map:
#                 left += 1
#             if s_arr[right] not in vowels_map:
#                 right -= 1
#             if s_arr[left] in vowels_map and s_arr[right] in vowels_map:
#                 temp = s_arr[left]
#                 s_arr[left] = s_arr[right]
#                 s_arr[right] = temp
#                 left += 1
#                 right -= 1
                
#             return ''.join(s_arr)

class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        n=len(s)
        left=0
        right=n-1
        vowels=set('AEIOUaeiou')
        while left<right:
            while left<right and s[left] not in vowels:
                left+=1
            while left<right and s[right] not in vowels:
                right-=1
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        s=''.join(s)
        return s