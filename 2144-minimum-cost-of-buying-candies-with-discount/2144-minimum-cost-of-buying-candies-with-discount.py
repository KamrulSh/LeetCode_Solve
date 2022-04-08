class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # ------------- Approach 1
        '''
        total = 0
        count = 0
        cost = sorted(cost)[::-1]
        for i in range(len(cost)):
            count += 1
            if count % 3 == 0:
                continue
            total += cost[i]
        return total
        '''
        # ------------- Approach 2
        cost.sort(reverse = True)
        total = 0
        for i in range(len(cost)):
            if i % 3 != 2:
                total += cost[i]
        return total
    