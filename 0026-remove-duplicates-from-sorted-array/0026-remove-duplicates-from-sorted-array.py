class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        assign to pinters left tp 0 and right to 1
        if there values at the left and right are equal, 


        """
        w, r = 1, 1
        while r < len(nums):
            if nums[w- 1] != nums[r]:
                copy = nums[r]
                nums[w] = copy
                w += 1
            r += 1
        return w
        