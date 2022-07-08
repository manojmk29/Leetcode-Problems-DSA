class Solution:
    def kthSmallest(self, mat , k: int) -> int:
        arr=[]
        n=len(mat)
        if(k==1):
            return(mat[0][0])
        if(k==n*n):
            return(mat[n-1][n-1])
        for i in range(n):
            for j in range(n):
                if(len(arr)<k):
                    heapq.heappush(arr,-mat[i][j])
                else:
                    if(arr[0]<-mat[i][j]):
                        heapq.heappop(arr)
                        heapq.heappush(arr,-mat[i][j])
        return(-arr[0])
        