class Solution:
    def countSubstrings(self, s: str) -> int:
        ln = len(s)
        palindrome_count = 0
        table = [[0 for i in range(ln)] for i in range(ln)]

        i = 0
        maxLength = 1
        while i < ln:
            table[i][i] = 1
            palindrome_count += 1
            i += 1

        i = 0
        while i < ln - 1:
            if s[i] == s[i + 1]:
                table[i][i + 1] = 1
                palindrome_count += 1
            i += 1

        str_len = 3
        while str_len <= ln:
            init = 0
            while init < ln - str_len + 1:
                end = init + str_len - 1
                if s[init] == s[end] and table[init + 1][end - 1] == 1:
                    table[init][end] = 1
                    palindrome_count += 1
                init += 1
            str_len += 1

        return palindrome_count
