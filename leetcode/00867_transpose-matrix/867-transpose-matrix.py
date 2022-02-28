class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        ll = len(matrix[0])
        count = 0
        while count < ll:
            row = []
            for i in range(len(matrix)):
                row.append(matrix[i][count])
            transpose.append(row)
            count += 1

        return transpose
