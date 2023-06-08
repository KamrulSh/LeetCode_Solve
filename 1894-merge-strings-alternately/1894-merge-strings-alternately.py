class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        minVal = 0
        w1, w2 = False, False
        if l1 <= l2:
            minVal = l1
            w1 = True
        else:
            minVal = l2
            w2 = True
            
        merge = ""
        for i in range(minVal):
            merge += word1[i] + word2[i]
            
        if w1 == False:
            merge += word1[minVal:]
        else:
            merge += word2[minVal:]
        
        return merge
        