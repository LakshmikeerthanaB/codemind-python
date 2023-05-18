

n=int(input())
x=65+n-1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(x),end=" ")
    x=x-1
    print( )
