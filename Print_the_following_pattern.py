n=int(input())
x=1
for i in range(1,n+1):
    for j in range(x,n+1):
        print(j,end=" ")
    x=i+1
    print()
