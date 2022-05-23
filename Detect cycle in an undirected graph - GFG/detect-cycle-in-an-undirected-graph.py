class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, arr):
        check={}
        for i in range(V):
            check[i]=False
        def dfs(node,parent):
            if(check[node]):
                return(True)
            check[node]=True
            for i in arr[node]:
                if i!=parent:
                    if(dfs(i,node)):
                        return(True)
            return(False)
        for i in range(V):
            if check[i]==False:
                if(dfs(i,None)):
                    return(True)
        return(False)

#{ 
#  Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends