class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row in range(numRows):
            arr = [None] * (row+1)
            arr[0], arr[-1] = 1, 1
            for col in range(1, row):
                arr[col] = triangle[row-1][col] + triangle[row-1][col-1]

            triangle.append(arr)
        return triangle
