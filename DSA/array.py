#use array module
print("array module")
import array

a= array.array('i',[1,4,7,5,3])
print("value at 4th place",a[4])
#print elements
for i in a:
    print(i)

print("using numpy")
import numpy as np

b=np.array([7,8,1,2,5,6,3])
print("value at 5th place",b[5])
for i in b:
    print(i)
#end of single-D array

#Multi-D array
print("Multi-D array")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("value at 1 row 2th place",arr[1, 2])
for row in arr:
    for elem in row:
        print(elem)

print(dir())