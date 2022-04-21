class Solution:
    def checkRecord(self, s: str) -> bool:
        # --------------- Approach 1
        '''
        count1, count2 = 0, 0
        for i in s:
            if i == 'L':
                count1 += 1
                if count1 >= 3:
                    return False
            else:
                count1 = 0
                if i == 'A':
                    count2 += 1
                if count2 >= 2:
                    return False
        return True
        '''
        # --------------- Approach 2
        rule1 = s.count('A') < 2
        rule2 = s.count('LLL') == 0
        return rule1 and rule2