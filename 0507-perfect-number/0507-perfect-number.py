# class Solution:
#     def checkPerfectNumber(self, num: int) -> bool:
#         result = 1
        
#         for i in range(2, (num//2) + 1):
#             if (num % i) == 0:
#                 result += i
                
#         return result == num

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        if num <= 1:
            return False

        limit = int(sqrt(num) + 1)
        sum = 0
        for i in range(1, limit):
            if num % i == 0:
                if num / i == i:
                    sum += i
                else:
                    sum += i
                    if i != 1:
                        sum += num / i
        return sum == num