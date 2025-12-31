class Solution:
    def minOperations(self, logs: List[str]) -> int:
        par = "../"
        sameFolder = "./"
        operations = []
        for log in logs:
            if log == sameFolder:
                continue
            elif log == par:
                if operations:
                    operations.pop()
            else:
                operations.append(log)
        return len(operations)



        