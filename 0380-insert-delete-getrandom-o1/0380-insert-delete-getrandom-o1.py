class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.data = []
        

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.data.append(val)
            self.dict[val] = len(self.data)-1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.data:
            last_item = self.data[-1]
            idx_rmv = self.dict[val]

            self.data[idx_rmv] = last_item
            self.dict[last_item] = idx_rmv
            self.dict.pop(val)
            self.data.pop()
            return True  
        else:
            return False

    def getRandom(self) -> int:
        # ran = random.randint(0, len(self.data))
        # return self.data[ran-1]
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()