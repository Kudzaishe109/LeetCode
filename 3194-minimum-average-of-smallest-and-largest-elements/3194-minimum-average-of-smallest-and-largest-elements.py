class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        """
        #Understand
            I - [int]

            O - float

            E - if nums is empty return 0
              - if nums has 1 elemt return that element

        #Plan
        initialize an empyt list, averages
        sort num in ascending order
        intialize two pointers l = 0 and r = len(nums) - 1
        loop through nums as long as r > l:
            append the average of l and r to the averages
            move my pointers inwards
        return min(averages)

        #Implement
        """
        averages = []
        l, r = 0, len(nums) - 1
        nums.sort()
        while r > l:
            averages.append((nums[l] + nums[r]) / 2)
            r -= 1
            l += 1
        return min(averages)

        