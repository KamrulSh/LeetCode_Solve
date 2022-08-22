class Solution:
    def reverseBits(self, n: int) -> int:
        bit_str = "{0:032b}".format(n)
        rev_str = bit_str[::-1]
        return int(rev_str, 2)
