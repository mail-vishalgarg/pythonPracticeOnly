"""
[[1,2,3],          [[7,4,1],
 [4,5,6],   ==>     [8,5,2],
 [7,8,9]]           [9,6,3]]
"""

def rotate(matrix):
    #Reverse the matrix first
    matrix.reverse()

    for i in range(len(matrix)):
        for j in range(i):
            #Swap the matrix elements here
            matrix[i][j], matrix[j][i]  = matrix[j][i],matrix[i][j]

    return matrix

print rotate([[1,2,3],
              [4,5,6],
              [7,8,9]])
