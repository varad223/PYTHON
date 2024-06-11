acc=int(input("enter a no"))
cac=int(input("enter a no"))
cca=int(input("enter a no"))
if (acc>cac)and(cac>cca):
    print("greater no is :",acc)
elif (cac>cca)and(cca>acc):
    print("greater no is :",cac)
else:
  print("greater no is :",cca)
