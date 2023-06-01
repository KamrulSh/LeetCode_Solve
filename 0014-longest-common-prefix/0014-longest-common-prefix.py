class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        length = min(len(s) for s in strs)
        
        prefix = ""
        for i in range(length):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return prefix
            prefix += strs[0][i]
            
        return prefix