class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        count = 2
        while count <= numRows:
            prev_row = result[-1]
            row = []
            row.append(1)
            for i in range(0, len(result[-1]) - 1):
                row.append(prev_row[i] + prev_row[i + 1])
            row.append(1)
            result.append(row)
            count += 1
        return result


        