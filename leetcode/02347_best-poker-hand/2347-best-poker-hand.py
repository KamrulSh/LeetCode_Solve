class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        counter1 = Counter(ranks)
        counter2 = Counter(suits)
        maxVal1, maxVal2 = 0, 0
        for i, val in counter1.items():
            maxVal1 = max(maxVal1, val)
        for i, val in counter2.items():
            maxVal2 = max(maxVal2, val)

        if maxVal2 == 5:
            return "Flush"
        elif maxVal1 >= 3:
            return "Three of a Kind"
        elif maxVal1 == 2:
            return "Pair"
        else:
            return "High Card"
