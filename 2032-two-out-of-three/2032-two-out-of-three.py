class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        table = {}
        for i in nums1:
            if i not in table:
                table[i] = {1}
                
        for i in nums2:
            if i not in table:
                table[i] = {2}
            else:
                table[i].add(2)
        
        for i in nums3:
            if i not in table:
                table[i] = {3}
            else:
                table[i].add(3)

        li = []
        for i in table:
            if len(table[i]) >= 2:
                li.append(i)
        return li
            