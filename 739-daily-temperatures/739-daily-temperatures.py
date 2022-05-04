class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        stk=[]
        for i in range(n):
            while(stk and temperatures[stk[-1]]<temperatures[i]):
                popped=stk.pop()
                ans[popped]=i-popped
            stk.append(i)
        return(ans)
        
        
        
        # stk=[]
        # ret=[]
        # hmap={}
        # n=len(temperatures)
        # for i in range(n-1,-1,-1):
        #     cnt=1
        #     cur=temperatures[i]
        #     while(stk and stk[-1][1]<=cur):
        #         cnt+=1
        #         cnt+=hmap[stk[-1][0]]
        #         stk.pop()
        #     hmap[i]=cnt-1
        #     cnt=cnt if(stk) else 0
        #     ret.append(cnt)
        #     stk.append((i,cur))
        # return(ret[::-1])