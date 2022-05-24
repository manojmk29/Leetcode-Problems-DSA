#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        check=[0 for i in range(V)]
        visited=[0 for i in range(V)]
        def dfs(node):
            if(visited[node]):
                return(False)
            check[node]=True
            visited[node]=True
            for i in adj[node]:
                if(check[i]):
                    return(True)
                if(dfs(i)):
                    return(True)
            check[node]=False
            return(False)
        for i in range(V):
            if(not visited[i]):
                if(dfs(i)):
                    return True
        return False
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends