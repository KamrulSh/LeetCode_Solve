class Solution:
    def findLucky(self, arr: List[int]) -> int:
        table = collections.Counter(arr)
        maxVal = -1
        for idx, val in table.items():
            if idx == val:
                maxVal = max(maxVal, idx)
        return maxVal
