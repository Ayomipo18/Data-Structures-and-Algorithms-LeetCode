class Solution:
    '''
    time - O(nlogn)
    space - O(n)
    where n is the lenght of nums
    case 1 : [1,2,3] -> [1,3,2] -> all asc, swap last two values
    case 2 : [3,2,1] -> all desc, swap from both ends
    case 3 : [2,1,3] -> [2,3,1]
    case 4 : [2,1,6,4,8] -> [2,1,6,8,4]
    case 5 : [2,1,6,9,8] -> [2,1,8,6,9]
    case 5 : [2,1,6,4,3,2,1] -> [2,2,1,1,3,4,6] 
    case 6 : [2,1,1,2,3,4,6] -> [2,1,2,1,3,4,6]
    - basically, two cases
    case 1 : if all desc; [4,3,2,1], no peak, then swap the values and return
    case 2 : if there is peak(from taking rightmost peak), from that rightmost peak-1, find number to the right that is greater than peak-1
    HOW TO SWAP
    - swap the pair with the lowest weightage to get next greater sequence(swap the last peak with left element)
    -case, all in desc order, just swap
    [  1,   2,    3,    2,    3]
    [10^4, 10^3, 10^2, 10^1, 10^0]
    '''
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return nums

        peak, i = -1, 1

        while i < len(nums):
            if nums[i] > nums[i-1]:
                peak = i
            i += 1

        if peak == -1:
            for i in range(len(nums)//2):
                self.swap(i, len(nums)-1-i, nums)
            return nums

        i, index = peak + 1, peak

        while i < len(nums):
            if nums[i] > nums[peak-1] and nums[i] < nums[peak]:
                index = i
            i += 1

        self.swap(peak-1, index, nums)
        nums[peak:] = sorted(nums[peak:])

        return nums

    def swap(self, left, right, nums):
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp