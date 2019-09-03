n = int(input())
l = input().split()
count = 0
for i in range(n):
    count = l.count(l[i])
    if count == 1:
        ans = l[i]
print(ans)
