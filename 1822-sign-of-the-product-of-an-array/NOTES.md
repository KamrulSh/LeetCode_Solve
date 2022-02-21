# using reduce

```py
from operator import mul
from functools import reduce
class Solution:
    def arraySign(self, nums: List[int]) -> int:

        op = reduce(mul, nums)

        if op == 0:
            return 0
        elif op <0:
            return -1
        else:
            return 1
```

# using sign multiplication

```py
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign = sign * -1
        return sign
```
