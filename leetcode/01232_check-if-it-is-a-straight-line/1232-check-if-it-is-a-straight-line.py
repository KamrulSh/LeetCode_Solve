class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        dx = coordinates[1][0] - coordinates[0][0]  # dx = x2-x1
        dy = coordinates[1][1] - coordinates[0][1]  # dy = y2-y1

        # dy / dx = y-y1 / x-x1
        # dy * (x-x1) = dx * (y-y1)
        for i in range(2, len(coordinates)):
            lhs = dy * (coordinates[i][0]-coordinates[0][0])
            rhs = dx * (coordinates[i][1]-coordinates[0][1])
            if lhs != rhs:
                return False
        return True
