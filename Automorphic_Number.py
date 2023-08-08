import math
n=int(input())
st=len(str(n))
sq=n*n
x=pow(10,st);
sqmod=(sq)%x
if(sqmod==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")