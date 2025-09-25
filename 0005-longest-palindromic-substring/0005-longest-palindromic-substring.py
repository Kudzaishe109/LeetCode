class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_len = 0
        for i in range(len(s)):
            r_move, l_move = i, i
            while r_move < len(s) and l_move >= 0 and s[r_move] == s[l_move]:
                if r_move - l_move + 1 > result_len:
                    result = s[l_move: r_move + 1]
                    result_len = r_move - l_move + 1
                r_move += 1
                l_move -= 1
            r_move, l_move = i + 1, i 
            while r_move < len(s) and l_move >= 0 and s[l_move] == s[r_move]:
                if r_move - l_move + 1 > result_len:
                    result = s[l_move: r_move + 1]
                    result_len = r_move - l_move + 1
                r_move += 1
                l_move-= 1
        return result
                







        