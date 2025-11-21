class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqmap = {}
        for num in nums:
            freqmap[num] = freqmap.get(num, 0) + 1

        items = list(freqmap.items())
            items.sort(key=itemgetter(0), reverse=True)
        items.sort(key=itemgetter(1))
        result = []
        for num, count in items:
            result.extend([num] * count)
        
        return result