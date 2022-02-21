# problem

https://leetcode.com/problems/longest-palindrome/

# using hashtable

```py
class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = {}
        for i in s:
            if i not in table:
                table[i] = 1
            else:
                table[i] += 1

        count = 0
        one = 0
        for e in table:
            if table[e] % 2 == 1:
                count += table[e] - 1
                table[e] = 1
                one = 1
            else:
                count += table[e]
        count += one
        return count
```

# using set()

```py
class Solution:
    def longestPalindrome(self, s: str) -> int:
        table_set = set()
        for i in s:
            if i not in table_set:
                table_set.add(i)
            else:
                table_set.remove(i)

        if len(table_set) > 0:
            length = len(s) - len(table_set) + 1
        else:
            length = len(s)
        return length
```

# using enumerate

```py
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
