class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        00 01 02
        10 11 12
        20 21 22
        
        00 10 20
        01 11 21
        02 12 22
        """
        
        m=len(matrix)
        for i in range(m):
            for j in range(m):
                if(i<j):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(m-1//2):
            for j in range(m//2):
                matrix[i][j],matrix[i][m-j-1]=matrix[i][m-j-1],matrix[i][j]