n = int(input())
l = [int(x) for x in input().split()]
oe = []
for i in l:
    oe.append(i%2)
#print(*oe)
if oe.count(1) > oe.count(0): r= 0
else: r = 1
if 1 not in oe or 0 not in oe:print(-1)
else:
    for i in l:
        if i%2==r:
            print(i)
            break
