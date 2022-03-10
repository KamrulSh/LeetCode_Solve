class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        val = 999999
        index = -1
        for i in range(len(points)):
            if x == points[i][0] or y == points[i][1]:
                distance = abs(x-points[i][0]) + abs(y-points[i][1])
                if distance < val:
                    val = distance
                    index = i
        return index

        # ------------- method 2

        # validDists = {}
        # for i, point in enumerate(points):
        #     if point[0] == x or point[1] == y:
        #         validDists[i] = abs(point[0] - x) + abs(point[1] - y)

        # return min(validDists, key=validDists.get, default=-1)
