class Solution:
    # #[0,0,2,1]            3          1           2         3
    # def conquer(self, arr, arr1_start, arr1_end, arr2_start, arr2_end):
    #     while arr1_start <= arr1_end and arr2_start <= arr2_end:
    #         if arr[arr1_start] > arr[arr2_start]:
    #             temp = arr[arr1_start]
    #             arr[arr1_start] = arr[arr2_start]
    #             arr[arr2_start] = temp

    #         arr1_start += 1

    # def divide(self, arr, start, end):
    #     if start == end:
    #         return
    #     mid = start + ((end - start) // 2)
    #     left, right = mid, mid + 1
    #     self.divide(arr, start, left)
    #     self.divide(arr, right, end)
    #     self.conquer(arr, start, left, right, end)

    # def sortColors(self, nums: List[int]) -> None:
    #     self.divide(nums, 0, len(nums)-1)

    def sortColors(self, nums: List[int]) -> None:
        #time - O(n)
        left, right = 0, len(nums) - 1
        index = 0
        while index <= right:
            if nums[index] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                left += 1
                index += 1

            elif nums[index] == 1:
                index += 1

            else:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
        