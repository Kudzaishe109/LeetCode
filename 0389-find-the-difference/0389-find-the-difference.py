class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        p = 0
        while p < len(s):
            if s[p] != t[p]:
                return t[p]
            p += 1
        return t[-1]
        