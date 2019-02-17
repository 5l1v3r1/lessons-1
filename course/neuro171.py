import numpy as np

X = np.array([[1,60], [1,50], [1,75]])
Y = np.array([[10], [7], [12]])
step1 = X.T.dot(X)
step2 = np.linalg.inv(step1)
step3 = step2.dot(X.T)
B = step3.dot(Y)
print(X)
print(Y)
print(B)