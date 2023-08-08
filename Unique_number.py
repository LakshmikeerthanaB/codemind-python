n=int(input())
st=str(n)
c=0
for i in range(len(st)):
    for j in range(len(st)):
        if(i!=j):
            if(st[i]==st[j]):
                c=c+1
if(c==0):
    print("Unique Number")
else:
    print("Not Unique Number")