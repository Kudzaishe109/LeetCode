class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True

        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and typed[j] == name[i] :
                j += 1
                i += 1
            elif typed[j] == typed[j - 1] and j > 0:
                j += 1
            else:
                return False
        return i == len(name)
