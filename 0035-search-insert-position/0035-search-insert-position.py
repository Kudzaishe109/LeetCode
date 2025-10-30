class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, len(nums) - 1)
    def helper(self, nums, target, left, right):
        mid = (left + right) // 2
        if right < left:
            return left

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return self.helper(nums, target, mid + 1, right)
        else :
            return self.helper(nums, target, left, mid - 1)
    

