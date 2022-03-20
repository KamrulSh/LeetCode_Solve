class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dict = {}
        newArr = []
        for num in arr:
            count = 0
            number = num
            while num != 0:
                if num & 1 == 1:
                    count += 1
                num >>= 1
            if count not in dict:
                dict[count] = [number]
            else:
                dict[count].append(number)
        # print(dict)
        dictIdx = sorted(dict)
        # print(dictIdx)
        
        for i in dictIdx:
            newArr.extend(sorted(dict[i]))
        # print(newArr)
        return newArr
        
        '''
        Output:
        {2: [10, 3, 5, 6], 3: [100, 7], 6: [1000], 5: [10000], 0: [0], 1: [1, 2, 4, 8, 1024, 512, 256, 128, 64, 32, 16]}
        [0, 1, 2, 3, 5, 6]
        [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 3, 5, 6, 10, 7, 100, 10000, 1000]
        '''