class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda v: v[1], reverse=True)
        # print(boxTypes)
        total = 0
        for box, unit in boxTypes:
            if truckSize > box:
                truckSize -= box
                total += box * unit
            else:
                total += truckSize * unit
                break
        return total
