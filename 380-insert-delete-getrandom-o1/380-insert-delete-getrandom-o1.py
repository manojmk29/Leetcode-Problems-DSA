class RandomizedSet(object):

    def __init__(self):
        self.hmap={}
        self.harr=[]
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hmap:
            return(False)
        n=len(self.harr)
        self.harr.append(val)
        self.hmap[val]=n       
        return(True)
    
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hmap:
            return(False)
        val_index=self.hmap[val]
        last=self.harr[-1]
        self.hmap[last]=val_index
        self.harr[val_index]=last
        self.hmap.pop(val)
        self.harr.pop()
        return(True)
    def getRandom(self):
        """
        :rtype: int
        """
        return(random.choice(self.harr))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()