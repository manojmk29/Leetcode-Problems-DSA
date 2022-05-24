class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        check=[0 for i in range(len(graph))]
        def dfs(node,last):
            if check[node]!=0 :
                if check[node]==last:
                    return(False)
                return(True)
            check[node]=last*-1
            for i in graph[node]:
                if(dfs(i,check[node])==False):
                    return(False)
            return(True)
        for i in range(len(graph)):
            if(check[i] ==0 and dfs(i,1)==False):
                    return(False)
        return(True)
            