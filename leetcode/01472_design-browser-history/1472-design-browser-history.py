class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.position = 0
        self.visited = False

    def visit(self, url: str) -> None:
        if self.visited == True:
            popped = len(self.stack)-1-self.position
            for i in range(popped):
                self.stack.pop()
        self.stack.append(url)
        self.position = len(self.stack)-1
        # print("vi", self.position, self.stack[self.position])

    def back(self, steps: int) -> str:
        self.visited = True
        pos = self.position - steps
        self.position = pos if pos > 0 else 0
        # print("bk", self.position, self.stack[self.position])
        return self.stack[self.position]

    def forward(self, steps: int) -> str:
        self.visited = True
        pos = self.position + steps
        self.position = pos if pos < len(self.stack) else len(self.stack)-1
        # print("fw", self.position, self.stack[self.position])
        return self.stack[self.position]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

'''
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7],["goo.com"],["face.com"],["tube.com"],[2],[1],[3],["linkedin.com"],[1],[2],[4]]
------------------------------------------------
stdout:
func, self.position, self.stack[self.position]

vi 1 google.com
vi 2 facebook.com
vi 3 youtube.com
bk 2 facebook.com
bk 1 google.com
fw 2 facebook.com
vi 3 linkedin.com
fw 3 linkedin.com
bk 1 google.com
bk 0 leetcode.com
vi 1 goo.com
vi 2 face.com
vi 3 tube.com
bk 1 goo.com
bk 0 leetcode.com
fw 3 tube.com
vi 4 linkedin.com
fw 4 linkedin.com
bk 2 face.com
bk 0 leetcode.com
------------------------------------------------
Outout:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com",null,null,null,"goo.com","leetcode.com","tube.com",null,"linkedin.com","face.com","leetcode.com"]

'''
