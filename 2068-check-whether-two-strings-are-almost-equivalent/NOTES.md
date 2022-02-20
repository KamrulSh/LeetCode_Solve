# using ord()

```py
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        arr1 = [0] * 26


        for word in word1:
            idx = ord(word) - 97
            arr1[idx] += 1

        for word in word2:
            idx = ord(word) - 97
            arr1[idx] -= 1

        for i in range(26):
            if abs(arr1[i]) > 3:
                return False

        return True
```

# using dict get()

```py
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c = {}
        for l in word1:
            c[l] = c.get(l,0)+1
        for l in word2:
            c[l] = c.get(l,0)-1
        for k in c:
            if abs(c[k]) > 3:
                return False
        return True
```
