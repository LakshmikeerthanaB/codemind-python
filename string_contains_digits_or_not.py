n=int(input())
for i in range(1,n+1):
    a=input()
    count=0
    for i in a:
        if i in"1234567890":
            count+=1
    if(count>0):
        print("Yes")
    else:
        print('No')