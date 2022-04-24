class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        # ---------------- Approach 1
        '''
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
        '''

        # ------------------- Approach 2
        m = len(s)
        direc = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
        upmost = startPos[0] + 1
        downmost = n - startPos[0]
        leftmost = startPos[1] + 1
        rightmost = n - startPos[1]
        curr_row, curr_col = 0, 0
        next_row, next_col = {0: m}, {0: m}
        ans = []

        for i in range(m-1, -1, -1):
            curr_row -= direc[s[i]][0]
            curr_col -= direc[s[i]][1]
            maxstep = m-i
            if curr_row - upmost in next_row:
                maxstep = min(maxstep,  next_row[curr_row - upmost] - i - 1)
            if curr_row + downmost in next_row:
                maxstep = min(maxstep,  next_row[curr_row + downmost] - i - 1)
            if curr_col - leftmost in next_col:
                maxstep = min(maxstep,  next_col[curr_col - leftmost] - i - 1)
            if curr_col + rightmost in next_col:
                maxstep = min(maxstep,  next_col[curr_col + rightmost] - i - 1)
            next_row[curr_row] = i
            next_col[curr_col] = i
            ans.append(maxstep)

        return ans[::-1]
