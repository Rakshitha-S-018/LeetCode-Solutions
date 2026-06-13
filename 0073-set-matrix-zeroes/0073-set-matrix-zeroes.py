class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)#rows
        n=len(matrix[0]) #cols
        
        row=set() #Suppose a row has multiple zeros, With a list:The same row is stored twice.With a set:Only one copy is stored.
        col=set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)

        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j]=0
        

