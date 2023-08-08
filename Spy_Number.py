n=int(input())
q=1
s=0
while(n!=0):
    r=n%10
    s=s+r
    q=q*r
    n=n//10
if(s==q):
    print("Spy Number")
else:
    print("Not Spy Number")