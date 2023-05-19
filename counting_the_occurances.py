a=input()
x=input()
count=0
for i in a:
    if(i==x):
        count+=1
if(count>0):
    print(count)
else:
    print('-1')