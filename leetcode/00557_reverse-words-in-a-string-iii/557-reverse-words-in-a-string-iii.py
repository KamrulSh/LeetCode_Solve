class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        s = s.split()
        for item in s:
            strr = ""
            for i in item:
                strr = i + strr
            arr.append(strr)
        arr = " ".join(arr)
        return arr
