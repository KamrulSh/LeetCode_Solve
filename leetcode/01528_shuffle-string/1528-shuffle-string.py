class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ll = len(indices)
        newStr = [None] * ll

        for i in range(ll):
            newStr[indices[i]] = s[i]

        return "".join(newStr)
