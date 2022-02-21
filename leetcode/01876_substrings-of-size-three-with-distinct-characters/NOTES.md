# using set

```py
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        if len(s) < 3:
            return count
        for i in range(len(s)-2):
            subStr = set(s[i:i+3])
            if len(subStr) == 3:
                count += 1
        return count
```
