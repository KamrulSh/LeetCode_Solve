class Solution:
    def trimMean(self, arr: List[int]) -> float:
        '''
        arr = sorted(arr)
        ll = len(arr)
        perc5 = int(0.05 * ll)
        arr[:perc5] = [0] * perc5
        arr[-perc5:] = [0] * perc5
        avg = sum(arr) / (ll-perc5*2)
        return avg
        '''
        # ------------- approach 2
        ll = len(arr)
        perc5 = int(0.05 * ll)
        arr = sorted(arr)[perc5:ll-perc5]
        avg = sum(arr) / len(arr)
        return avg
