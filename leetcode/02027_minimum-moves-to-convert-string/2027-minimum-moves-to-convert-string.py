class Solution:
    def minimumMoves(self, s: str) -> int:
        count = 0
        ll = len(s)
        arr = []
        for i in range(ll):
            if len(arr) == 3:
                count += 1
                arr = []
            if s[i] == "X" and len(arr) < 3:
                arr.append(s[i])
            elif s[i] == "O" and arr:
                arr.append(s[i])
        return count+1 if arr else count
