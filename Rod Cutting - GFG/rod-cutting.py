#User function Template for python3
# from functools import lru_cache
# class Solution:
#     def cutRod(self, price, n):
#         @lru_cache(None)
#         def helper(ind,val):
#             if(ind==0):
#                 return(val*price[ind])
#             notake=helper(ind-1,val)
#             take=-float("inf")
#             if(ind+1<=val):
#                 take=price[ind]+helper(ind,val-ind+1)
#             return(max(take,notake))
#         return(helper(n-1,n))
            
from functools import lru_cache
class Solution:
    def cutRod(self, price, n):
        @lru_cache(None)
        def helper(ind,val):
            if(ind==0):
                return(val*price[ind])
            notake=helper(ind-1,val)
            take=-float("inf")
            rodLength = ind+1
            if(rodLength<=val):
                take=price[ind]+helper(ind,val-rodLength)
            return(max(take,notake))
        return(helper(n-1,n))           

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends