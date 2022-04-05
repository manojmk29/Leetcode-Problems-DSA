class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def helper(tot):
            if(tot==0):
                return(0)
            if(tot<0):
                return(float("inf"))
            ret=float("inf")
            for i in coins:
                if(i<=tot):
                    ret=min(ret,1+helper(tot-i))
            return(ret)
        val=helper(amount)
        return(val if val!=float("inf") else -1)