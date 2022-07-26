class Solution:
    def countAsterisks(self, s: str) -> int:
        new = s.split("|")
        count = 0
        for i in range(0, len(new), 2):
            for j in new[i]:
                if j == "*":
                    count += 1
        return count
