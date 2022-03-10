class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        value = 0
        for acc in accounts:
            total = sum(acc)
            if total > value:
                value = total
        return value
