class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        new_nums = []
        for num in nums:
            if not new_nums:
                new_nums.append(num)
            if num != new_nums[-1]:
                new_nums.append(num)
            count = 0 
        for i in range(1, len(new_nums) - 1):
            if new_nums[i-1] < new_nums[i] and new_nums[i] > new_nums[i + 1]:
                count += 1
            if new_nums[i-1] > new_nums[i] and new_nums[i] < new_nums[i + 1]:
                count += 1
        return count
        
        