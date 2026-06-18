class RandomizedSet:

    def __init__(self):
        self.nums=[]
        self.pos={}
        
        

    def insert(self, val):
        if val in self.pos:
            return False 
        else:
            self.pos[val]=len(self.nums)#returns last pos to insert
            self.nums.append(val)
            return True

    def remove(self, val):
        if val not in self.pos:
            return False
        else:
            idx=self.pos[val]
            last=self.nums[-1]

            self.nums[idx]=last
            self.pos[last]=idx

            self.nums.pop()
            del self.pos[val] #deleted pos 
            
            return True
        

    def getRandom(self) :
        if len(self.nums)>0:
            return random.choice(self.nums)
        else:
            return None
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()