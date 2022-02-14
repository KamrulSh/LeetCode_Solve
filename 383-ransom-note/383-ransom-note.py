class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1={}
        d2={}
        for x in ransomNote:
            d1[x] = d1.get(x,0)+1

        for x in magazine:
            d2[x] = d2.get(x,0)+1
            
        for x in d1:
            if x not in d2 or d1[x] > d2[x]:
                return False
            
        return True