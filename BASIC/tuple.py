flowers=("rose", "lotus", "sunflower", "lily", "hibiscus")
print("tuple is :",flowers)
print("rose" in flowers)
print("grapes" in flowers)
print("lily" not in flowers)
#change in tuple
t1=(46,5,78,99,[3,13])
print("tupple is :",t1)
t1[4][-1]=43
print("tupple is :",t1)
t1=(56,67,56,75,877,[343,344])
print("tupple is :",t1)
del t1[-1][0]
print("tupple is :",t1)
t1.count(56)
print(t1.index(56))
