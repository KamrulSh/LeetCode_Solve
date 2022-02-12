class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        table = []
        for email in emails:
            em = ""
            plus = False
            for i in range(len(email)):
                if email[i] == ".":
                    continue
                elif email[i] == "+":
                    plus = True
                elif email[i] == "@":
                    em += email[i:]
                    break
                elif plus == True:
                    continue
                else:
                    em += email[i]
                    
            if em not in table:
                table.append(em)
                    
        # print(table)
        l = len(table)
        return l