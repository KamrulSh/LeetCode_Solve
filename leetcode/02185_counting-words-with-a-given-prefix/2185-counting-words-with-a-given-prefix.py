class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        ll = len(pref)
        for word in words:
            # if word.startswith(pref):
            #     count += 1

            if word[:ll] == pref:
                count += 1

        return count
