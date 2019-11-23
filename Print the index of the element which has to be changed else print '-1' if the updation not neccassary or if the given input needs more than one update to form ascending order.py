n = int(input())
l = [int(x) for x in input().split()]
a = []
a.extend(l)
a.sort()
if a == l:
    cond1=True
else:
    cond1 = False
count = 0
for i in range(n-1):
    if l[i] > l[i+1]:
        count+=1
if count>1:
    cond2 = True
else:
    cond2 = False
if cond1 or cond2:
    print(-1)
else:
    for i in range(n-1):
        if l[i]>l[i+1]:
            print(i)
            break
