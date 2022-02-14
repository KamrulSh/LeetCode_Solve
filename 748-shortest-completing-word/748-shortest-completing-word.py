class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = []
        for i in licensePlate:
            if i.isalpha():
                letters.append(i.lower())
        words.sort(key=len)
        # print(letters, words)
        
        for word in words:
            flag = True
            for letter in letters:
                if letter not in word or letters.count(letter) > word.count(letter):
                    flag = False
                    break
            if flag == True:
                return word
    