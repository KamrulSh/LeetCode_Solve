class Solution:
    def reverseString(self, str: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # recursive
        i = 0
        j = len(str) - 1

        def reverseHelper(left, right):
            if left < right:
                str[left], str[right] = str[right], str[left]
                reverseHelper(left+1, right-1)

        reverseHelper(i, j)
