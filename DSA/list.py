list=[1,2,3,"kbc",7,"oop","#",2.8]
print(list)
for i in enumerate(list):
    print(i)
print("Mult-D list")
a=[[1,2,4,"v"],["a","r",2.7]]
print(a)
print(list[-2])#indexing
print(list[3])
list.append(4)#insert
list.extend(a)
print(list+a)#concatinate
print(list*2)
print(list[2:-1])#slicing
print(a.pop(0))
for i in enumerate(a):
    print(i)