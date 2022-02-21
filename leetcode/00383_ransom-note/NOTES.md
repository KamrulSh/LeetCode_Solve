# using string replace

```py
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
            magazine = magazine.replace(i, "", 1)
        else:
            return False
        return True
```

​

# collections.Counter()

```py
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_stat = collections.Counter(ransomNote)
        magazine_stat = collections.Counter(magazine)
        # print(magazine_stat, ransomNote_stat)
        return magazine_stat >= ransomNote_stat
```

# another collections.Counter()

```py
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = collections.Counter(ransomNote)
        count2 = collections.Counter(magazine)
        count2.subtract(count)
        for key in count2:
            if count2[key] < 0:
                return False
        ​
        return True
```
