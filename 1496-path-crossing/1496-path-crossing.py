class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y = 0,0
        location = set()
        location.add((0,0))
        for p in path:
            if p == "N":
                x,y = x,y+1
            elif p == "S":
                x,y = x,y-1
            elif p == "E":
                x,y = x+1,y
            else:
                x,y = x-1,y
            
            if (x,y) not in location:
                location.add((x,y))
            else:
                return True
            
        return False
        