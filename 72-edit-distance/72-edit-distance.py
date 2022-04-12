class Solution:
    def minDistance(self, word1: str, word2: str) :
        m=len(word1)
        n=len(word2)
        arr=[i for i in range(n+1)]
        for i in range(1,m+1):
            new=[]
            for j in range(0,n+1):
                if(j==0):
                    new.append(i)
                else:
                    if(word1[i-1]==word2[j-1]):
                        new.append(arr[j-1])
                    else:
                        new.append(1+min(arr[j-1],arr[j],new[j-1]))
            arr=new
        return(arr[n])
    
    
#         @lru_cache(None)
#         def helper(i,j):
#             if(i==0):
#                 return(j)
#             if(j==0):
#                 return(i)
#             if(word1[i-1]==word2[j-1]):
#                 return(helper(i-1,j-1))
#             p=1+helper(i-1,j-1)
#             q=1+helper(i,j-1)
#             r=1+helper(i-1,j)
#             return(min(p,q,r))
#         return(helper(m,n))
        