class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            first_pointer = 0
            second_pointer = 1
            while second_pointer <= len(nums) - 1:
                if nums[first_pointer] > nums[second_pointer]:
                    nums[first_pointer] , nums[second_pointer] = nums[second_pointer], nums[first_pointer]
                second_pointer += 1
                first_pointer += 1
