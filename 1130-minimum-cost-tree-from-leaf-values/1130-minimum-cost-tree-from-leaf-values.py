class Solution: 
    def mctFromLeafValues(self, arr) -> int:      
        n=len(arr)
        dp=[[-1 for i in range(n)]for i in range(n)]
        def helper(l,r):
            if(dp[l][r]!=-1):
                return(dp[l][r])
            if(l==r):
                dp[l][r]=(arr[l],0)
                return((arr[l],0))
            ans=(0,float("inf"))
            for i in range(l,r):
                left=helper(l,i)
                right=helper(i+1,r)
                cur_sum=left[0]*right[0]+left[1]+right[1]
                cur_max=max(left[0],right[0])
                if(ans[1]>cur_sum):
                    ans=(cur_max,cur_sum)
            dp[l][r]=ans
            return(ans)
        return(helper(0,n-1)[1])
