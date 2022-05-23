class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            f=bisect.bisect_right(i,target)
            if(i[f-1]==target):
                return(True)
        return(False)
        