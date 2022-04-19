class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ret=[]
        n=len(boxes)
        for i in range(n):
            if(boxes[i]=="1"):
                ret.append(i)
        ar=[]
        for i in range(n):
            val=0
            for j in ret:
                val+=abs(i-j)
            ar.append(val)
        return(ar)
        