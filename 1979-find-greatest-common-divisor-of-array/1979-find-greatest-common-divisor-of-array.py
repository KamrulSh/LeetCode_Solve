class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)
        gcd = 0
        
        while(maxi != mini):
            if maxi > mini:
                maxi -= mini
            elif mini > maxi:
                mini -= maxi
                
        return mini