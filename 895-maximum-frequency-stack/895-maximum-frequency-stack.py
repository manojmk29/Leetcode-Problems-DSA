class FreqStack:

    def __init__(self):
        self.value=defaultdict(int)
        self.freq=defaultdict(list)
        self.maxf=0
    def push(self, val: int) -> None:
        temp=self.value[val]
        temp+=1
        self.value[val]=temp
        self.freq[temp].append(val)
        self.maxf=max(self.maxf,temp)
    def pop(self) -> int:
        stack=self.freq[self.maxf]
        val=stack.pop()
        if(not stack):
            self.maxf-=1
        self.value[val]-=1
        return(val)

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()