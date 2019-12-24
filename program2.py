import numpy as l
import numpy.matlib
a=l.array(input("enter 1st  2*2 matrix::"));
b=l.array(input("enter 2nd  2*2 matrix::"));
print "first matrix you entered::\n",a;
print "second matrix you entered::\n",b;
print "addition of matrix 1,2::\n",l.add(a,b);
print "subtraction of matrix 1,2::\n",l.subtract(a,b);
print "multiplication of matrix 1,2::\n",l.multiply(a,b);
print "division of matrix 1,2::\n",l.divide(a,b);
print "dot of matrix 1,2::\n",l.dot(a,b);
print "transpose of matrix 1::\n",l.transpose(a);
print "transpose of matrix 2::\n",l.transpose(b);
print "det of matrix 1::\n",l.linalg.det(a);
print "det of matrix 2::\n",l.linalg.det(b);
print "inverse of matrix 1::\n",l.linalg.inv(a);
print "inverse of matrix 2::\n",l.linalg.inv(b);
print "eigen vector of matrix 1::\n",l.linalg.eig(a);
print "eigen vector of matrix 2::\n",l.linalg.eig(b);
print "eigen value of matrix 1::\n",l.linalg.eigvals(a);
print "eigen value of matrix 2::\n",l.linalg.eigvals(b);
print "rank of matrix 1::\n",l.linalg.matrix_rank(a);
print "rank of matrix 2::\n",l.linalg.matrix_rank(b);
print "QR decomposition of matrix 1::\n",l.linalg.qr(a);
print "QR decomposition of matrix 2::\n",l.linalg.qr(b);
print "power 3 of matrix 1::\n",l.linalg.matrix_power(a,3);
print "power 3 of matrix 2::\n",l.linalg.matrix_power(b,3);
print "solving  matrix 1,2::\n",l.linalg.solve(a,b);
print "identity of matrix::\n",l.matlib.identity(5, dtype = float);
print "eye of matrix::\n",l.matlib.eye(n = 3, M = 4, k = 0, dtype = float);
print "randomness of matrix::\n",l.matlib.rand(3,3);

