class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        '''
        count = 0
        ll = len(word)
        caps = False
        if ord(word[0]) >= 65 and ord(word[0]) <= 90:
            caps = True
        for w in word:
            ww = ord(w)
            if ww >= 65 and ww <= 90:
                count += 1
        if count == 0 or (caps == True and (ll == count or count == 1)):
            return True
        else:
            return False
        '''

        # ----------- approach 2
        if word.isupper() or word.islower():
            return True
        elif word[0].isupper() and all(w.islower() for w in word[1:]):
            return True
        else:
            return False

        # return (word.upper() == word) or (word.title() == word) or (word.lower() == word)

        # return len(word) == 1 or word.isupper() or word[1:].islower()

        # ----------- approach 5
        '''
        i = word.upper() 
        j = word.lower()
        k = word.capitalize()
        if i==word or j==word or k==word:
            return True
        return False
        '''
