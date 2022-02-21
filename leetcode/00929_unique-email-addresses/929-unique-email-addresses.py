class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmail = set()
        for email in emails:
            local, domain = email.split("@")
            name = local.split("+")[0].replace(".", "")
            uniqueEmail.add(name + "@" + domain)

        l = len(uniqueEmail)
        return l
