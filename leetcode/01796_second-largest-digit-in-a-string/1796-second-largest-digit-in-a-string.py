class Solution:
    def secondHighest(self, s: str) -> int:
        digit = set()
        for i in s:
            if i.isdigit():
                digit.add(i)
        digit = sorted(digit)
        ll = len(digit)
        if ll < 2:
            return -1
        else:
            return digit[-2]
