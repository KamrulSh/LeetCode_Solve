# using enumerate
```
class Solution:
def longestPalindrome(self, s: str) -> int:
chars = set()
res = 0
for i, char in enumerate(s):
if char in chars:
res += 2
chars.remove(char)
else:
chars.add(char)
if res < len(s):
res += 1
return res
```