class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # ------------- approach 2 (Monotonic Stack) => O(n)
        stack = []
        table = {}
        for val in nums2:
            while stack and val > stack[-1]:
                table[stack.pop()] = val
            stack.append(val)
            # print(stack, table)
        res = []
        for x in nums1:
            res.append(table.get(x, -1))
        return res

        # ------------- approach 1 O(n^2)
        """
        ll = len(nums2)
        ans = []
        for val in nums1:
            idx = nums2.index(val)
            for j in range(idx, ll):
                if nums2[j] > val:
                    ans.append(nums2[j])
                    break
            else:
                ans.append(-1)
        return ans
        """
