### Used stack and dictionary

Basically the problem says, if in nums1 we are working on 4, then in nums2 first find where is 4 and from that index find the next number greater than 4 in nums2. We can see that the solution is always coming from the reverse side of the list nums2. This should tell us to use stack.

Steps:

- We traverse nums2 and start storing elements on the top of stack.
- If current number is greater than the top of the stack, then we found a pair. Keep popping from stack till the top of stack is smaller than current number.
- After matching pairs are found, push current number on top of stack.
- Eventually when there are no more elements in nums2 to traverse, but there are elements in stack, we can justify that next bigger element wasn't found for them. Hence we'll put -1 for the remaining elements in stack.

```py
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    res = []
    stack = []
    mapping = {}

    for n in nums2:
        while stack and n > stack[-1]:
            mapping[stack.pop()] = n
        stack.append(n)

    while stack:
        mapping[stack.pop()] = -1

    for n in nums1:
        res.append(mapping[n])

    return res
```
