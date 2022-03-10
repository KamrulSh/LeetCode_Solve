class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashSet = {}
        for item in s:
            if item not in hashSet:
                hashSet[item] = 1
            else:
                hashSet[item] += 1

        for pos, val in enumerate(s):
            if hashSet[val] == 1:
                return pos
        return -1
