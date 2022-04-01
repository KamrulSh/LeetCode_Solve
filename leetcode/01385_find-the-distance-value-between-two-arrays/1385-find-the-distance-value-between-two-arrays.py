class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                diff = abs(arr1[i] - arr2[j])
                if diff <= d:
                    break
            else:
                count += 1
        return count
