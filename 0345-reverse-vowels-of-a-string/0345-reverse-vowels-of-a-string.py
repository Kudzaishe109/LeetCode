class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        def is_vowel(ch):
            return ch in "aeiouAEIOU"

        i, j = 0, len(s) - 1

        while i < j:
            if not is_vowel(s[i]):
                i += 1
                continue
            if not is_vowel(s[j]):
                j -= 1
                continue
            # both are vowels → swap
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return "".join(s)
