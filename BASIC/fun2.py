def spsdfdm(a,b):
    c=a+b
    d=a*b
    e=a-b
    f=a/b
    g=a//b
    h=a%b
    return c,d,e,f,g,h
print("this is a function program for arethmatic operation")
no1=int(input("enter no1"))
no2=int(input("enter no2"))
s,p,q,r,t,v=spsdfdm(no1,no2)
print("sum= ",s)
print("product= ",p)
print("substraction= ",q)
print("division= ",r)
print("floor division= ",t)
print("modulus= ",v)
