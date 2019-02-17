import urllib
from urllib import request
import numpy as np

#fname = 'https://stepic.org/media/attachments/lesson/16462/boston_houses.csv'
fname = input()  # read file name from stdin
f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with
#вытянем Y умножив на [1,0,0 ... 0]
tm = np.zeros((data.shape[1],1))
tm[0][0] = 1
Y = data.dot(tm)

#вытянем X умножив на [0,1,1 ... 1] ...
#X = np.delete(data, 0, axis=1)
X = data
for i in range(X.shape[0]):
    X[i][0]=1


step1 = X.T.dot(X)
step2 = np.linalg.inv(step1)
step3 = step2.dot(X.T)
B = step3.dot(Y)

#print(B)
for i in range(B.shape[0]):
    print(str(B[i][0]),end=' ')
