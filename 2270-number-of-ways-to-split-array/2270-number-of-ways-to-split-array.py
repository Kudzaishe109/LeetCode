class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        right_sum = 0
        left_sum = sum(nums)
        for i in range(0, len(nums) - 1):
            right_sum += nums[i]
            left_sum -= nums[i]
            if right_sum >= left_sum:
                count += 1
        return count



