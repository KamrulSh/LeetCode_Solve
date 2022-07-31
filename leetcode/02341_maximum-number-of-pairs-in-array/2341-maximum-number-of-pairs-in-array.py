class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dicti = Counter(nums)
        ll = len(dicti)
        pairs, leftover = 0, 0
        for key, val in dicti.items():
            pairs += val//2
            leftover += val % 2
        return [pairs, leftover]
