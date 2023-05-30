class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)[::-1]
        count = 0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                count += 1
            else:
                break
        return count