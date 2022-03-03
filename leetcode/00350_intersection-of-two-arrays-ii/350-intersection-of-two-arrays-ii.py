class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # using 2 pointer
        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        store = []
        l1 = len(nums1)
        l2 = len(nums2)

        while pt1 < l1 and pt2 < l2:

            if nums1[pt1] > nums2[pt2]:
                pt2 += 1
            elif nums1[pt1] < nums2[pt2]:
                pt1 += 1
            else:
                store.append(nums1[pt1])
                pt1 += 1
                pt2 += 1

        return store
