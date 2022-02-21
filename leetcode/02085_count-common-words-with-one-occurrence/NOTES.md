# Using Python Counter Objects

```py
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1, w2 = Counter(words1), Counter(words2)
        count = 0
        for i in words1:
            if w1[i] == 1 and w2[i]==1:
                count +=1
        return count
```

​

# Using hashtable

```py
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        table = {}
        for w in words1:
            if w not in table:
                table[w] = "1"
            else:
                table[w] += "1"
        for w in words2:
            if w not in table:
                table[w] = "2"
            else:
                table[w] += "2"
        count = 0
        for word in table:
            if table[word] == "12":
                count += 1
        return count
```
