class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # --------------- Approach 1
        '''
        substr = []
        for word in words:
            count = 0
            for st in words:
                if word in st:
                    count += 1
                # print(count, word, st)
                if count == 2:
                    substr.append(word)
                    break
        return substr
        '''
        
        # --------------- Approach 2
        result = set()
        for i, substr in enumerate(words):
            for j, word in enumerate(words):
                if substr in word and i != j:
                    result.add(substr)
        return result