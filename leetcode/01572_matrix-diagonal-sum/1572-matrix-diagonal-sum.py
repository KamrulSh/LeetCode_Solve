class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ll = len(mat)
        half = ll // 2
        j = ll-1
        total = 0
        for i in range(ll):
            if i == half and ll % 2 == 1:
                total += mat[i][i]
                j -= 1
            else:
                total += mat[i][i] + mat[i][j]
                i += 1
                j -= 1
        return total
