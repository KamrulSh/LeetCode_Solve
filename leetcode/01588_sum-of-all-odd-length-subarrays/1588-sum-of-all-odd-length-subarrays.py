class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l = len(arr)
        total = 0
        for length in range(1, l+1, 2):
            for i in range(l-length+1):
                total += sum(arr[i:i+length])
                # print(i, arr[i:i+length], total)
        return total
