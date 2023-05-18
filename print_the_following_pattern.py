n=int(input())
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for l in range(0,n):
        if(i==1 or i==n or l==0 or l==n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()