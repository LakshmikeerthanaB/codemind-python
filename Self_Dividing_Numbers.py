def fun(n):
    st1=str(n)
    ls=[]
    c=0
    for i in st1:
        ls.append(i)
    for i in ls:
        if(int(i)!=0 and n%int(i)==0):
            c=c+1
    if(c==len(ls)):
       return 1
    else:
       return 0
n=int(input())
m=int(input())
for i in range(n,m+1):
    if(fun(i)==1):
        print(i,end=' ')