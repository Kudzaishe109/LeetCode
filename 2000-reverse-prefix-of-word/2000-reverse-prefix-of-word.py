class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        word = list(word)
        l, r = 0, word.index(ch)
        while l < r:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
        return "".join(word)

        