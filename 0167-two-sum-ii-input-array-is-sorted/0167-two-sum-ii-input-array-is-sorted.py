class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complements = {}
        for idx, num in enumerate(numbers):
            comp = target - num
            if comp in complements:
                return [complements[comp] + 1, idx +1]
            complements[num] = idx
            