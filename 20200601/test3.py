import numpy as np

arr = np.empty((8,4))
print(arr)

#팬시색인 : 팬시색인은 슬라이싱과 달리 데이터를 새로운 배열로 복사한다.
for i in range(8):
    arr[i] = i

print(arr)
print(arr[[4,3,0,6]]) #왜이렇게 될까 arr[4,3,0,6]은 에러나는 이유.확인ok
print(arr[4],arr[3],arr[0],arr[6])

arr2 = np.arange(32).reshape((8,4))
print(arr2)

print(arr2[[1,5,7,2]])
print(arr2[[1,5,7,2],[0,3,1,2]])

print(arr2[[1,5,7,2]][:,[0,3,1,2]]) # 지정된배열[[index]][:,[index'(index'기준으로 순서바꿔서 소환)]]


