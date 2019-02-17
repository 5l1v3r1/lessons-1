import numpy as np
mat = np.eye(3, 4, k=0)*2+np.eye(3, 4, k=1)
print(mat)
mat = mat.reshape(12,1)
print(mat)