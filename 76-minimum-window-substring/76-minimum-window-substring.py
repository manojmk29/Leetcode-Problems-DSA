class Solution(object):
    def minWindow(self,s,t):
        check=collections.defaultdict(int)
        for i in t:
            check[i]+=1
        need=len(check)
        l=0
        le=len(s)
        mint=float("inf")
        have=0
        ret=[-1,-1]
        temp=collections.defaultdict(int)
        for r,val in enumerate(s):
            if(val in check):
                temp[val]+=1
            if(val in check and temp[val]==check[val]):
                have+=1
            while(have==need):
                lr=r-l+1
                if(lr<mint):
                    mint=lr
                    ret=[l,r]
                val=s[l]
                if(val in check):
                    temp[val]-=1
                if(val in check and temp[val]<check[val]):
                    have-=1
                l+=1
        l,r=ret
        return(s[l:r+1] if(mint!=float("inf")) else "")
                    
                