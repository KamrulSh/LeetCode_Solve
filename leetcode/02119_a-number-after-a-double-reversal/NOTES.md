# using reverse procedure

```py
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        initial = num
        final = 0
        for i in range(2):
            rev_num = 0
            while num != 0:
                rem = num % 10
                rev_num = rev_num * 10 + rem
                num //= 10
            num = final = rev_num

        if initial == final:
            return True
        else:
            return False

```

# one line

```py
class Solution:
  def isSameAfterReversals(self, num: int) -> bool:
    return num == 0 or num % 10 != 0
```

# string reverse

```py
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        new = str(num)
        new_1 = new[::-1]
        new3 = new_1.lstrip('0')
        new_2 = new3[::-1]
        new4 = new_2.lstrip('0')
        return new == new4
```
