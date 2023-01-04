class Solution:
    '''
    use a dictionary to store freq of each number
    foreach number in the map, if a number is 1, return -1
    foreach number, do a freq // 3, if the remainder modulo 2 gives 0, add that to our count
    do a freq // 2, if it gives 0, awesome
    else return a -1 immediately
    '''
    def minimumRounds(self, tasks: List[int]) -> int:
        dict = {}
        rounds = 0
        
        for task in tasks:
            if task not in dict:
                dict[task] = 0
            dict[task] += 1
        
        print(dict)
        for key,val in dict.items():
#             three_check = val // 3
#             three_remainder = val % 3
#             two_check = val // 2
#             two_remainder = val % 2
#             print(key)
#             if three_remainder % 2 == 0:
#                 rounds += three_check + (three_remainder // 2)
#             elif:
                
#             elif two_remainder == 0:
#                 rounds += two_check
#             else:
#                 return -1
            #print("rounds ", rounds)
            # while val > 0:
            #     print("val ", val)
            #     print(" ")
            #     if val % 3 == 0:
            #         rounds += (val // 3)
            #         val %= 3
            #     elif val % 2 == 0:
            #         rounds += (val // 2)
            #         val %= 2
            #     else:
            if val == 1:
                return -1
            if val % 3 == 0:
                rounds += (val // 3)
            elif val % 3 == 1:
                rounds += ((val - 4) // 3) + 2
            elif val % 3 == 2:
                rounds += (val // 3) + 1
        return rounds if rounds > 0 else -1
        