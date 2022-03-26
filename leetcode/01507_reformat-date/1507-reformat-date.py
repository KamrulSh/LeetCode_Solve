class Solution:
    def reformatDate(self, date: str) -> str:
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        yy = date[-4:]
        mm = month.index(date[-8:-5]) + 1
        mm = "0" + str(mm) if mm < 10 else str(mm)
        dd = int(date[:-11])
        dd = "0" + str(dd) if dd < 10 else str(dd)
        output = yy + "-" + mm + "-" + dd
        return output
