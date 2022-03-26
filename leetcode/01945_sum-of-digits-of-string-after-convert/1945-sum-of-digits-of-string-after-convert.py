class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digit = ""
        for i in s:
            digit += str(ord(i)-96)

        count = 1
        while count <= k:
            val = 0
            for i in digit:
                val += int(i)
            digit = str(val)
            count += 1

        return int(digit)
