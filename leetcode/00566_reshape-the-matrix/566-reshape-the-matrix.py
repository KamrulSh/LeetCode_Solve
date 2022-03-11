class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # count of rows & columns of initial matrix
        row = len(mat)
        col = len(mat[0])
        newmat = []
        # if the product of rows & cols of mat and the new matrix are not same then return original matrix
        if row*col != r*c:
            return mat

        arr = []
        newcol = 0
        # Traversing the mat matrix and storing the its values in new matrix column wise
        for i in range(row):
            for j in range(col):
                arr.append(mat[i][j])
                newcol += 1
                # if the newcol value reached then empty the arr and set the newcol value to 0
                if newcol == c:
                    newmat.append(arr)
                    arr = []
                    newcol = 0

        return newmat
