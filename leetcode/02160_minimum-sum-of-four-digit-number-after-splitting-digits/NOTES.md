# using number calculation

```py
class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        while num != 0:
            digits.append(num % 10)
            num = num // 10

        digits.sort()
        total = 10*(digits[0] + digits[1]) + digits[2]+digits[3]
        return total
```

# using

```py
class Solution:
    def minimumSum(self, num: int) -> int:
      numList = []
      while num > 0:
        numList.append(num%10)
        num //= 10
      res = 0
      numList.sort()
      res += sum(numList[2:])
      res += sum(numList[:2])*10
      return res
```
