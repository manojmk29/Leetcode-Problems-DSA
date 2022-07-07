class Solution:
    def findClosestNumber(self, arr: List[int]) -> int:
        n=len(arr)
        neg=float("-inf")
        pos=float("inf")
        for i in arr:
            if(i==0):
                return(0)
            if(i<0):
                neg=max(neg,i)
            else:
                pos=min(pos,i)
        if(neg+pos==0):
            return(pos)
        if(abs(neg)<abs(pos)):
            return(neg)
        else:
            return(pos)