class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # using list
        rows = [list() for i in range(9)]
        cols = [list() for i in range(9)]
        boxs = [list() for i in range(9)]

        for i in range(len(board)):
            for j in range(len(board)):
                element = board[i][j]

                # for calculating box index
                k = (i//3) * 3 + (j//3)

                if element != ".":
                    if element not in rows[i]:
                        rows[i].append(element)
                    else:
                        return False

                    if element not in cols[j]:
                        cols[j].append(element)
                    else:
                        return False

                    if element not in boxs[k]:
                        boxs[k].append(element)
                    else:
                        return False

        return True
