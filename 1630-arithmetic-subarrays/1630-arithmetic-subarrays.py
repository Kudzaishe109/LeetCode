class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            interest_slice = nums[l[i] : r[i] + 1]
            interest_slice.sort()
            condition = True
            for x in range(2, len(interest_slice)):
                diff = interest_slice[1] - interest_slice[0]
                if diff != interest_slice[x] - interest_slice[x - 1]:
                    condition = False
                    break
            result.append(condition)
        return result
        