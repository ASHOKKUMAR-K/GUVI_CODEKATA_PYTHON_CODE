n = int(input())
l = input().split()
ln = len(l)
count = 0
ans = 0
for i in range(0, n):
    count = l.count(l[i-1])
    if count == int(l[i]):
        ans = i
print(ans)
