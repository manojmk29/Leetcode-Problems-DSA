#User function Template for python3


class Solution:
    def isCyclic(self, V, adj):
        from collections import deque
        indegree=[0 for i in range(V)]
        for i in adj:
            for j in i:
                indegree[j]+=1
        que=deque([])
        ret=[]
        for i in range(V):
            if(indegree[i]==0):
                que.append(i)
        cnt=0
        while(que):
            popped=que.popleft()
            cnt+=1
            for i in adj[popped]:
                indegree[i]-=1
                if(indegree[i]==0):
                    que.append(i)
        return(cnt!=V)       
            

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