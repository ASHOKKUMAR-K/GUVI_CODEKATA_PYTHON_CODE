n =int(input())
l = [int(x) for x in input().split()]
ans = 0
for i in range(1, len(l)-1):
    if l[i] < l[i-1] and l[i] < l[i+1]:
        ans += min(l[i+1], l[i-1]) - l[i]
print(ans)
