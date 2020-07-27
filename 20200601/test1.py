import numpy as np
# a = np.array([1,2,3,4])
# print(a,a.shape,a.ndim)

# l = [[1,2],[3,4]]
# print(l[0][0])

# a1 = np.array([[1,2],[3,4]])
# print(a1,a1.shape,a1.ndim)

# l2 = [[[1,2],[2,3]]]
# a2 = np.array(l2)
# print(a2,a2.shape,a2.ndim)
# print(l2[0][0][1])

# student = np.dtype([('name','S20'),('age','i1')])
# print('student',student)
# a5 = np.array([('test1',20),('test2',30)],dtype = student)
# print('a5',a5)
# print('a5타입',a5,a5.shape,a5.ndim)

# a6 = np.empty([4,3],dtype=int)
# print('a6',a6)
# a7 = np.zeros((10,),dtype=np.int)
# print('a7',a7)
# a8 = np.ones([2,2],dtype=int)
# print('a8',a8)

# a9 = np.arange(10,dtype = float)
# print('a9',a9)
# a10 = np.arange(10,20,2)
# print('a10',a10)

# all = np.linspace(10,20,5)
# print('all',all)
# a12 = np.linspace(1,2,5)
# print('a12',a12)

a13 = np.array([5,7,3,4,5,1,9,3,2,6])
print('a13',a13)
a14 = slice(2,7,2)
print('a13 슬라이스',a13[a14])
print(a13[2:7:2]) #뭔말인지..

a15 = np.arange(10)
print(a15)
print('a15슬라이스',a15[2:4])

a16 = np.array([[1,2,3],[3,4,5],[4,5,6]])
print('a16',a16[1:])

#행 설정, 열 설정
x = np.array([[1,2],[3,4],[5,6]])
y = x[[0,1,2],[0,1,0]]
print(x)
print(y)

y2 = x[1:2,[0,1,0]]
print('y2',y2)

r = range(5)
lt = list(r)
print(iter(lt))

for i in iter(lt):
    print(i)

print('----------')
a17 = np.array([1,2,3,4])
for i in a17:
    print(i)

print('----------')
for i2 in np.nditer(a17):
    print(i2)

# list3 = [[1,2],[3,4]]
# for i2 in list3
#     print(i2)

# a18 = array(list3)
# for i2 in a18:
#     print(i2)

# print(a18.shape)
# for i2 in np.nditer(a18):
#     print(i2)

list4 = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
a19 = np.array(list4)
for i2 in a19:
    print(i2)

for i2 in np.nditer(a19):
    print(i2)