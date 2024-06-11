def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mult(a,b):
    return a*b
def fd(a,b):
    return a//b
def mod(x,y):
    return x%y

print("this is a function program for addition")
no1=int(input("enter no1"))
no2=int(input("enter no2"))
ans1=add(no1,no2)
print("addition:",ans1)
ans2=sub(no1,no2)
print("substraction:",ans2)
ans3=div(no1,no2)
print("division:",ans3)
ans4=mult(no1,no2)
print("multiplicaton",ans4)
ans5=fd(no1,no2)
print("floor division:",ans5)
ans6=mod(no1,no2)
print("modulus:",ans6)
