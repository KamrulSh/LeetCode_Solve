class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # ------------------ step 1.
        # if num == 0:
        #     return True
        # elif num % 10 == 0:
        #     return False
        # else:
        #     return True
        
        # ------------------ step 2
        # if num == 0: 
        #     return True
        # st = str(num).strip("0")
        # return st == str(num)
        
        # ------------------ step 3
        # if num == 0:
        #     return True
        # if str(num)[-1] == "0":
        #     return False
        # else:
        #     return True
        
        # ------------------ step 4
        if num == 0:
            return True
        rev1 = str(num)[::-1]
        rev1 = int(rev1)
        rev2 = str(rev1)[::-1]
        rev2 = int(rev2)
        return num == rev2