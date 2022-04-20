class Solution:
    def minOperations(self, boxes: str):
        n=len(boxes)
        ret=[0 for i in range(n)]
        one=0
        val=0
        for i in range(n):
            val+=one
            ret[i]=val
            one+=(boxes[i]=="1")
        one=0
        val=0
        for i in range(n-1,-1,-1):
            val+=one
            ret[i]+=val
            one+=(boxes[i]=="1")
        return(ret)