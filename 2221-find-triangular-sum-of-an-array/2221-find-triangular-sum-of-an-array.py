class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # base case
        if len(nums) == 1:
            return nums[-1]
        #recursive curse
        newNums = []
        for i in range(len(nums) - 1):
            newNums.append((nums[i] + nums[i + 1]) % 10)
        nums = newNums
        return self.triangularSum(nums)
        