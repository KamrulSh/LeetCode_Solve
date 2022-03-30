class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        strr = ""
        slen = len(s)
        for i in words:
            strr += i
            if len(strr) < slen:
                continue
            elif len(strr) == slen and strr == s:
                return True
            else:
                break
        return False
