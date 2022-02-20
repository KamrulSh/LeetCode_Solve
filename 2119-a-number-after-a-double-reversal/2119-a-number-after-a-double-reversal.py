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
        if num == 0:
            return True
        if str(num)[-1] == "0":
            return False
        else:
            return True