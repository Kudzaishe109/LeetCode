class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            -using a sliding window techniques
            -set left and right pointer to zero
            -right pointer should move forward by 1 regardless
            -if s[right] is in the window s[left:right] move left by 1
            longestSubString = max of longestSubString and right - left

        """
        window = set()
        left = 0
        longestSubString = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            
            window.add(s[right])

            longestSubString = max(longestSubString, right - left + 1)
        return longestSubString
            

        