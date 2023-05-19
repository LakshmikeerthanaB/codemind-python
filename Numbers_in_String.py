n=input()
count=0
for i in n:
    if i in '0123456789':
        count+=int(i)
print(int(count))