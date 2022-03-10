class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp = []
        for line in matrix:
            if target >= line[0] and target <= line[-1]:
                temp = line

        for i in temp:
            if i == target:
                return True
        return False
