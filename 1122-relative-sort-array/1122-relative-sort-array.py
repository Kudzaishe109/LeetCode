class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}
        end = []
        for num in arr1:
            if num not in arr2:
                end.append(num)
            freq[num] = freq.get(num, 0) + 1
        end.sort()
        result = []
        for num in arr2:
            result += [num] * freq[num]
        return result + end
            
        