#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here
        # hmap=collections.defaultdict(list)
        r=len(M)
        c=len(M[0])
        arr=[]
        for i in range(r):
            flag=1
            for j in range(c):
                if(M[i][j]==1):
                    flag=0
            if(flag==1):
                arr.append(i)
        j=-1
        for i in range(r):
            flag=1
            for j in arr:
                if(i!=j and M[i][j]==0):
                    flag=0
            if(flag==1):
                return(j)
        return(-1)
        
                


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