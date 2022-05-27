#User function Template for python3
class Solution:
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, v, adj):
        #code here
        import heapq
        key=[float("inf") for i in range(v)]
        pres=[False for i in range(v)]
        key[0]=0
        cnt=0
        while(cnt<v):
            cnt+=1
            val=float("inf")
            ind=-1
            for i in range(v):
                if(key[i]<val and pres[i]==False):
                    val=key[i]
                    ind=i
            pres[ind]=True
            for i in adj[ind]:
                if(pres[i[0]]==False and i[1]<key[i[0]]):
                    key[i[0]]=i[1]
        return(sum(key))
            
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends