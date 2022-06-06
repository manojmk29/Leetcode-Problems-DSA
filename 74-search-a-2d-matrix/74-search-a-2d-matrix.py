class Solution:
    def searchMatrix(self, matrix, tar: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        l=0
        e=r-1
        while(l<=e):
            mid=(l+e)//2
            val=matrix[mid][c-1]
            if(val>tar):
                e=mid-1
            elif(val<tar):
                l=mid+1
            else:
                return True
        if (l == r):
            return  False
        s=0
        e=c-1
        while s<=e:
            m=(s+e)//2
            val=matrix[l][m]
            if(val>tar):
                e=m-1
            elif(val<tar):
                s=m+1
            else:
                return(True)
        return(False)
                