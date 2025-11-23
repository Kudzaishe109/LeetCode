class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        for char, frequency in freq.items():
            if frequency == 1:
                return s.index(char)
        return -1