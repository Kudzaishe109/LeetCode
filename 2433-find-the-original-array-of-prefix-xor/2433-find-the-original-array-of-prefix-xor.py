class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = []
        arr.append(pref[0])
        i = 1
        while i < len(pref):
            arr.append(pref[i] ^ pref[i - 1])
            i += 1
        return arr
        