class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen :
                if numbers.index(num) == numbers.index(complement):
                    return [seen[complement]+ 1, numbers.index(num) + 2]
                return [seen[complement]+ 1, numbers.index(num) + 1]

            seen[num] = i 
        