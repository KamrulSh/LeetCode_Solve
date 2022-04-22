class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        answer = []
        for i in range(len(s)):
            row = startPos[0]
            col = startPos[1]
            count = 0
            # print("outer", i, s[i])
            for j in range(i, len(s)):
                if s[j] == "R":
                    col += 1
                elif s[j] == "L":
                    col -= 1
                elif s[j] == "U":
                    row -= 1
                elif s[j] == "D":
                    row += 1
                # print(row, col)
                if (row >= 0 and row < n) and (col >= 0 and col < n):
                    count += 1
                else:
                    break
            answer.append(count)
        return answer
