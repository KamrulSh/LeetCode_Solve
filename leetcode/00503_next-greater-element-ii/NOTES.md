### Approach #1

```py
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # (Monotonic stack)
        # storing the nums position in the stack instead of value
        stack = []
        nge = [-1] * len(nums)
        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                popVal = stack.pop()
                nge[popVal] = num
            stack.append(idx)
        '''
        2nd iteration is for those element that
        are remaining in the stack as it is circular
        '''
        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                popVal = stack.pop()
                nge[popVal] = num

        return nge
```

### Approach #2

```py
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums + nums
        records = []
        next_greater = [-1] * len(nums2)
        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]
            while records and records[-1] <= num:
                records.pop()
            if records:
                next_greater[i] = records[-1]
            records.append(num)

        return next_greater[:len(nums)]

```

### Approach #3

```py
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        s = []

        size = len(nums)
        res = [-1 for i in range(size)]

        for i in range(2 * size):
            i = i % size
            while len(s) != 0 and nums[s[-1]] < nums[i]:
                item = s.pop()
                res[item] = nums[i]
            s.append(i)

        return res
```

### Approach #4

Use the stack to record the reversed array nums. Loop the array from last integer to the first one. If the last integer in stack is bigger than the current interger in array, we have found the answer. Otherwise, we need to keep pop up the integer in stack. Besides, we need to push the current integer to the stack in each step.

```py
class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        ret = [-1] * n
        stack = nums[::-1]
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                ret[i] = stack[-1]
            stack.append(nums[i])
        return ret

```

### Approach #5

```py
class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        ret = [-1] * n
        stack1 = []
        stack2 = nums[::-1]
        for i in range(n - 1, -1, -1):
            while stack1 and stack1[-1] <= nums[i]:
                stack1.pop()
            if stack1:
                ret[i] = stack1[-1]
            else:
                while stack2 and stack2[-1] <= nums[i]:
                    stack2.pop()
                if stack2:
                    ret[i] = stack2[-1]
            stack1.append(nums[i])
        return ret
```

### Approach #6

```py
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        for _ in range(2):
            for i, e in enumerate(nums):
                while stack and e > nums[stack[-1]]:
                    res[stack.pop()] = e
                stack.append(i)
        return res
```

### Approach #7

```py
class Solution:
    def nextGreaterElements(self, nums):
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                index = (i+j)%len(nums)
                if nums[index] > nums[i]:
                    res.append(nums[index])
                    break
            if len(res) <= i:
                res.append(-1)
        return res
```
