class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = {}
        new_s = s.split()
        if len(pattern) != len(new_s):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in table:
                if new_s[i] in table.values():
                    return False
                table[pattern[i]] = new_s[i]

            elif table[pattern[i]] == new_s[i]:
                continue
            else:
                return False
        return True
