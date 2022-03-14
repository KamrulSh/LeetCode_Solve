class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # -------------- method 1 (inplace)

        ll = len(prices)
        for i in range(ll):
            for j in range(i+1, ll):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices

        # -------------- method 2 (using new list)

        # disc = []
        # ll = len(prices)
        # for i in range(ll):
        #     for j in range(i+1, ll):
        #         if prices[j] <= prices[i]:
        #             val = prices[i] - prices[j]
        #             disc.append(val)
        #             break
        #     else:
        #         disc.append(prices[i])
        # return disc
