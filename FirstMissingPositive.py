from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        # print("length:", length)
        hasOne = False
        for i in range(length):
            if nums[i] == 1:
                hasOne = True
            elif nums[i] <= 0 or nums[i] > length:
                nums[i] = 1
        if hasOne == False:
            return 1
        # print("After step 1:", nums)
        i = 0
        for i in range(length):
            if nums[(abs(nums[i]) - 1)] > 0:
                nums[(abs(nums[i]) - 1)] *= -1
                # print(nums, i)
        # print("After step 2:", nums)
        for i in range(length):
            result = length + 1
            if nums[i] > 0:
                result = i + 1
                break
        return result


# sol = Solution()
# print(sol.firstMissingPositive([1, 2, 1]))
# print(sol.firstMissingPositive([7, 8, 9, 11, 12]))
# print(sol.firstMissingPositive([7, -2, 3, 1, 2, 20, -5]))
# print(sol.firstMissingPositive([3, 4, -1, 1]))
