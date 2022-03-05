class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ll = len(t)
        last2 = ord(t[ll - 1])
        last1 = 0
        for i in range(len(s)):
            last1 += ord(s[i])
            last2 += ord(t[i])

        return chr(last2 - last1)

        # --------- method 2
        # diff = collections.Counter(t) - collections.Counter(s)
        # return list(diff.keys())[0]

        # --------- method 3
        # cs = Counter(s)
        # ct = Counter(t)
        # for char in ct:
        #     if char not in cs or cs[char] < ct[char]:
        #         return char
