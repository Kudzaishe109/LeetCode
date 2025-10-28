class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, len(nums) - 1, target)
    def helper(self, nums, low, high, target):
        if low > high:
            return -1

        mid = (low + high) // 2

        if target == nums[mid]:      # base case
            return mid
        elif target > nums[mid]:
            return self.helper(nums, mid + 1, high, target)
        else:
            return self.helper(nums, low, mid - 1, target)
        
