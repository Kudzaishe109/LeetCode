class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for char in operations:
            if char.lstrip("-").isdigit():
                scores.append(int(char))
            elif char == "C":
                scores.pop()
            elif char == "D":
                scores.append(scores[-1] * 2)
            elif char == "+":
                sum_ = scores[-1] + scores[-2]
                scores.append(sum_)
        return sum(scores)