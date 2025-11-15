class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        def letterFrequency(s, dictionary):
            for char in s:
                dictionary[char] = dictionary.get(char, 0) + 1
            return dictionary
        ran_dict = letterFrequency(ransomNote, {})
        mag_dict = letterFrequency(magazine, {})
        for key in ransomNote:
            if key not in mag_dict:
                return False
            if ran_dict[key] > mag_dict[key]:
                return False
        return True