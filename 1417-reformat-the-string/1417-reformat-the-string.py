class Solution:
    def reformat(self, s: str) -> str:
        count1, count2 = 0, 0
        pos1, pos2 = 0, 1
        ll = len(s)
        char, digit = [], []
        newStr = ""
        for i in s:            
            if i.isnumeric():
                digit.append(i)
            else:
                char.append(i)
        
        diff = len(char) - len(digit)
        
        if diff == 1:
            # digit[0], digit[-1] = digit[-1], digit[0]
            for i in range(len(digit)):
                newStr += char[i] + digit[i]
            newStr += char[-1]
        elif diff == -1:
            # digit[0], digit[-1] = digit[-1], digit[0]
            for i in range(len(char)):
                newStr += digit[i] + char[i]
            newStr += digit[-1]
        elif diff == 0:
            # digit[0], digit[-1] = digit[-1], digit[0]
            for i in range(len(char)):
                newStr += char[i] + digit[i]
        return newStr
