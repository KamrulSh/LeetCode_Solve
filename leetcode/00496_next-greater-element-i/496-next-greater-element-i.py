class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ll = len(nums2)
        ans = []
        for val in nums1:
            idx = nums2.index(val)
            found = False
            for j in range(idx, ll):
                if nums2[j] > val:
                    found = True
                    ans.append(nums2[j])
                    break
            if found == False:
                ans.append(-1)
        return ans
