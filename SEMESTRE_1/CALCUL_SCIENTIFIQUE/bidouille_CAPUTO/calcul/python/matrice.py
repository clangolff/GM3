from mpmath  import *
mp.dps=50
A = matrix([[1, 2], [3, 4]])
B = matrix([[-2, 4], [5, 9]])
C=matrix (([21, 22, 23], [11, 22, 33], [43, 77, 89]))
#ndArray[start_index: end_index ,  :]
#print 1st column
print(C[:,0])
#print 2nd column
print(C[:,1])
C[: , 3]
A*B
A**-1
norm(A, 2)
cond(A)
#transpose
A.T
eye(2) 
ones(2)
zeros(2)
A[1,1] = 1 + 1j
U, S, V = mp.svd_r(A)
print (U)
print (S)
print (V)

