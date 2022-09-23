# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random

class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap.keys():
            return False
        else:
            self.hashmap[val] = len(self.array)
            self.array.append(val)
            return True 

    def remove(self, val: int) -> bool:
        if val not in self.hashmap.keys():
            return False
        else:
            index_to_remove = self.hashmap[val]
            last_val = self.array.pop()
            if last_val != val:
                self.array[index_to_remove] = last_val
            self.hashmap[last_val] = index_to_remove
            self.hashmap.pop(val)
            return True
            
    def getRandom(self) -> int:
        return random.choice(self.array)
    

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()