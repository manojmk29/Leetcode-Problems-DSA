from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        @lru_cache
        def helper(ind,c):
            if(n-1==ind):
                if(c==1):
                    if(s[ind-1]=="0"):
                        return(0)
                    if(s[ind-1]=="2" and s[ind]<"7"):
                        return(1)
                    if(s[ind-1]<"2"):
                        return(1)
                    return(0)
                elif(c==0):
                    if(s[ind]=="0"):
                        return(0)
                    else:
                        return(1)
            if(c==1):
                if(s[ind-1]=="0"):
                    return(0)
                if(s[ind-1]=="2" and s[ind]>"6"):
                    return(0)
            if(s[ind]=="0" and c==0):
                return(0)
            tot=0
            if(s[ind]=="0" or s[ind]>"2"):
                tot+=helper(ind+1,0)
            else:
                tot+=helper(ind+1,0)
                if(c!=1):
                    tot+=helper(ind+1,1)
            return(tot)
        return(helper(0,0))