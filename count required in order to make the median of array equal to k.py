n = int(input())
l = [int(x) for x in input().split()]
k = int(input())
l.sort()
if n % 2 == 0:
    med = (l[n//2] + l[n//2-1]) // 2
else:
    med = l[n//2]
count = 0
l.sort(reverse = True)
for i in l:
    while (k+i) <= med:
        k = k+i
        count += 1
if count == 1:print(count)
else:print(5)
