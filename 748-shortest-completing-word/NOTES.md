# String

```py
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
```

# String isalpha() Method and defaultdict

```py
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        nPlate = defaultdict(int)
        for i in licensePlate:
            if i.isalpha():
                nPlate[i.lower()]+=1
        print(nPlate)
        words = sorted(words, key=lambda x: len(x))
        print(words)
        for word in words:
            w = defaultdict(int)
            for i in word:
                w[i]+=1
            flag = True
            for key in nPlate:
                if nPlate[key] > w[key]:
                    flag = False
            if flag:
                return word
```

# using array and dict

```py
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        dict={}
        result=[]
        licensePlate=licensePlate.lower()
        for x in licensePlate:
            if x.isalpha():
                if x in dict:
                    dict[x]+=1
                else:
                    dict[x]=1

        def indict(dict,x):

            for y in dict:
                if y not in x:
                    return False
                elif x.count(y)<dict[y]:
                    return False

            return True

        result=[x for x in words if indict(dict,x)]
        results=sorted(result, key=lambda k:len(k))

        return results[0]
```
