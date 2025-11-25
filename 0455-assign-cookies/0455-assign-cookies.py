class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        current_g = 0
        current_s = 0

        while current_g < len(g) and current_s < len(s):
            if s[current_s] >= g[current_g]:
                current_g += 1
            current_s += 1
        return count




        