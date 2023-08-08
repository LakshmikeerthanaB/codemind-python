n=int(input())
ls=[]
for i in range(1,n):
    if(n%i==0):
        ls.append(i)
if(n==sum(ls)):
    print("True")
else:
    print("False")