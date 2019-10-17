m,y = map(str, input().split())
y = int(y)
#print(m,y)
if m in ('February', ):
    if y % 4 == 0:   dm = 29
    else: dm = 28
elif m in ('April', 'June', 'September', 'November'):
    dm = 30
else:
    dm = 31
count = 0
for i in range(2, dm+1):
    f = []
    for j in range(1, i+1):
        if i % j == 0:
            f.append(j)
    if len(f)<=2:
        count+=1
print(count)
