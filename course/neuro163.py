import numpy as np

x_shape = tuple(map(int, input().split()))
X = np.fromiter(map(int, input().split()), np.int).reshape(x_shape)
y_shape = tuple(map(int, input().split()))
Y = np.fromiter(map(int, input().split()), np.int).reshape(y_shape)
if X.shape[1] == Y.shape[1]:
    Y = Y.T
    R = X.dot(Y)
    print(R)
else:
    print('matrix shapes do not match')