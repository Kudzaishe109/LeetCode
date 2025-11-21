class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ordered = sorted(nums)
        result = []
        for num  in nums:
            result.append(ordered.index(num))
        return result
        