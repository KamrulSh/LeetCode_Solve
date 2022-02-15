class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = {}
        for i in s:
            if i not in table:
                table[i] = 1
            else:
                table[i] += 1
                
        count = 0
        one = 0
        for e in table:
            if table[e] % 2 == 1:
                one = 1
            count += table[e] // 2 * 2
        count += one
        return count