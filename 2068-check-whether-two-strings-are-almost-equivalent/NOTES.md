# using ord()
```
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