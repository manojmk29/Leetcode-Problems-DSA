class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        ret=[]
        hmap={}
        n=len(temperatures)
        for i in range(n-1,-1,-1):
            cnt=1
            cur=temperatures[i]
            while(stk and stk[-1][1]<=cur):
                cnt+=1
                cnt+=hmap[stk[-1][0]]
                stk.pop()
            hmap[i]=cnt-1
            cnt=cnt if(stk) else 0
            ret.append(cnt)
            stk.append((i,cur))
        return(ret[::-1])