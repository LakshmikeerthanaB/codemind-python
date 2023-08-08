m=int(input())
n=int(input())
ls=[]
ls1=[]
for i in range(1,m):
    if(m%i==0):
        ls.append(i)
for i in range(1,n):
    if(n%i==0):
        ls1.append(i)
if(sum(ls)==n and sum(ls1)==m):
    print("Amicable")
else:
    print("Not Amicable")