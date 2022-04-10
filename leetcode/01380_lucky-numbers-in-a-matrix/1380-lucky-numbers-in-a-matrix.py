class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        maxval = 0
        for row in matrix:
            minval = min(row)
            minidx = row.index(minval)
            # print(minval, minidx)
            for col in matrix:
                # print('s', minval, col[minidx])
                if minval < col[minidx]:
                    break
            else:
                maxval = max(minval, maxval, col[minidx])

        return [] if maxval == 0 else [maxval]
