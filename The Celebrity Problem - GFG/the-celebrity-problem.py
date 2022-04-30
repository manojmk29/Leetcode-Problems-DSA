#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here
        # hmap=collections.defaultdict(list)
        r=len(M)
        c=len(M[0])
        st=0
        end=r-1
        cand=-1
        while(st<end):
            if(M[end][st]):
                end-=1
            else:
                st+=1
        cand=st
        if(cand==-1):
            return(-1)
        for i in range(c):
            if(i!=cand):
                if(M[cand][i] or M[i][cand]==0):
                    return(-1)
        return(cand)
        
        
                


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends