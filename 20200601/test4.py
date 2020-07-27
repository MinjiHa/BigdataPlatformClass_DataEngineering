import numpy as np

#배열전치와 축 바꾸기 : 데이터 복사 없음. 뷰만 바꿈
arr = np.arange(15).reshape((3,5))
print(arr)

t = arr.T # 행과 열이 서로 바뀜
print(t)

arr2 = np.random.randn(6,3)
print(arr2)
print(np.dot(arr2.T,arr2)) #??

arr3 = np.arange(16).reshape((2,2,4))
print(arr3)
print(arr3.transpose((1,0,2)))  
