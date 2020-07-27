import numpy as np
a = np.arange(3)
print(a.shape,a.ndim)
print(a)

a1 = a.reshape(1,3)
print(a1)
print(a1.shape,a1.ndim)

a2 = np.swapaxes(a1,0,1)
print(a2)

a3 = np.arange(6).reshape(1,2,3)
print('a3',a3)
print(a3.shape,a3.ndim)
a4 = np.swapaxes(a3,1,2)
print(a4)

a5 = np.swapaxes(a3,0,1)
print('a5',a5)
print(a5.shape,a5.ndim)

a6 = np.arange(6).reshape(2,3)
print(a6)
a7 = a6.T
print(a7)

a6 = np.arange(6).reshape(1,2,3)
print('a6',a6)
print(a6.shape,a6.ndim)
a7 = np.transpose(a6,(1,0,2))
a8 = a6.transpose((1,0,2))
print('a7',a7)
print(a7.shape,a7.ndim)
print('a8',a8)
print(a8.shape,a8.ndim)