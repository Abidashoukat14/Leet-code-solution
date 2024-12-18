class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        edge=len(matrix)
        top=0
        bottom=len(matrix)-1
        while top < bottom :
            for col in range(edge):
                temp = matrix[top][col]
                matrix[top][col]=matrix[bottom][col]
                matrix[bottom][col]=temp
            top += 1
            bottom -= 1
        for row in range(edge):
            for col in range(row+1,edge):
                temp=matrix[row][col]  
                matrix[row][col]=matrix[col][row] 
                matrix[col][row]=temp
        return matrix        

        
        