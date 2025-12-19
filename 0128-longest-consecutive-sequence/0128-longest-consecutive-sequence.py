class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Understand
            - input -> [int]
            -output -> int

            Edge cases:
            
            - if not nums, return 0
            - if nums has 1 element return 1
            -repeating charecters should be treated as one
        
        """
        numsSet = set(nums)
        longest = 0

        for num in numsSet:

            if num - 1 not in numsSet:
                length = 0 
                while (num + length) in numsSet:
                    length += 1
                longest = max(longest, length)
        return longest

        