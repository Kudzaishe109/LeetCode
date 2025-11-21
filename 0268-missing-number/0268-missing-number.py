class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(len(nums)):
            if nums[x] != x:
                return x
        return nums[-1] + 1
        