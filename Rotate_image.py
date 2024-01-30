# To rotate a matrix by 90 degrees clockwise
def rotate(matrix):
    """
    Given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
    DO NOT allocate another 2D matrix and do the rotation.
    """
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    
    # Reverse each row
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    
    return matrix

# Test the function
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))

# Rotate the matrix counterclockwise
def rotate_counterclockwise(matrix):
    """
    Given an n x n 2D matrix representing an image, rotate the image by -90 degrees (counterclockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
    DO NOT allocate another 2D matrix and do the rotation.
    """
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    
    # Reverse each column
    matrix.reverse()
    
    return matrix

# Test the function
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_counterclockwise(matrix))