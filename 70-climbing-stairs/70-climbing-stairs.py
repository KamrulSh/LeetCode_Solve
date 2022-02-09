class Solution:
    
    def __init__(self):
        self.memory = {}
        
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        # iterative bottom-up
        way = [0] * (n+1)
        way[1] = 1
        way[2] = 2
        for i in range(3, n+1):
            way[i] = way[i-1] + way[i-2]
        
        return way[n]