class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        total = 0
        count = 0
        cost = sorted(cost)[::-1]
        for i in range(len(cost)):
            count += 1
            if count % 3 == 0:
                continue
            total += cost[i]
        return total