class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, src):
        import heapq
        n=len(adj) 
        hq=[] 
        dist=[float("inf") for i in range(n)] 
        dist[src]=0
        hq.append((0,src))
        while(hq):
            val_dist,val=heapq.heappop(hq)
            for i in adj[val]:
                iv=i[0]
                id=i[1]
                cur_dis=id+val_dist
                if cur_dis < dist[iv]:
                    dist[iv]=cur_dis
                    heapq.heappush(hq,(cur_dis,iv))
        return(dist)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends