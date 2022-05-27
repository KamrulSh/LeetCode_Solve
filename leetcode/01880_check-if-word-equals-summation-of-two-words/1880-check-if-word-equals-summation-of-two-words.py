class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # --- method 1
        '''
        l1 = len(firstWord)
        l2 = len(secondWord)
        l3 = len(targetWord)
        fw = ""
        sw = ""
        tw = ""
        for i in range(l1):
            val = ord(firstWord[i]) - 97
            fw += str(val)
        for i in range(l2):
            val = ord(secondWord[i]) - 97
            sw += str(val)
        for i in range(l3):
            val = ord(targetWord[i]) - 97
            tw += str(val)
        if int(fw) + int(sw) == int(tw):
            return True
        else:
            return False
        '''

        # --- method 2
        # ord(a)=97
        num_1 = "".join(str(ord(i)-97) for i in firstWord)
        num_2 = "".join(str(ord(i)-97) for i in secondWord)
        num_3 = "".join(str(ord(i)-97) for i in targetWord)
        return int(num_1)+int(num_2) == int(num_3)
