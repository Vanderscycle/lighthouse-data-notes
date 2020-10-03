import numpy as np

x = np.array([1, 2, 3, 4])
print(x)

# Matrix A
A = np.array([[1,2],[3,4],[5,6]])
print(type(A))

# in which the result is a tuple of (columns, rows)|(3x,2y) of the matrix
print(A.shape)
print(x.shape)
print(len(x)) # returns the length of the array (#in the list)

# transpose an a matrix

A_T = A.T
# this format is also acceptable
A_T = A.transpose()
print(A_T.shape)

# Note: the transpose of a matrix (At) can be obtained by reflecting the elements along its main diagonal
# https://en.wikipedia.org/wiki/Transpose

# Do not confuse transposition (flipping) with the invest of a matrix (a-1). NOTE non square matrices cannot have an inverse matrix because 

B = np.array([[2, 5], [7, 4], [4, 3]])
C = A + B
print(C)
print(C + 1)


# dot product
A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[2], [4]])
print(A.shape,B.shape)
C = A.dot(B)

# we change the space
# C = A . B (3,2) . (2, 1) = 3d vector (3,1)
print(C)

# identity matrix
# A-1 * A = I. This provides a way to cancel the linear transformation

I = np.eye(3) # similar to np.identity(n) but you can shift the index of the diagonal
IA = I.dot(A)
print(IA)

#determinant
#area
# non square matrices should be viewed geometrically as transformations between dimensions
M = np.array([[1,2],[3,4]])
det_M = np.linalg.det(M)
print(det_M)

# inverse matrices
A = np.array([[3, 0, 2], [2, 0, -2], [0, 1, 1]])
A_inv = np.linalg.inv(A)
I = A_inv.dot(A)
print(I)