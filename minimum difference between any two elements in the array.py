n = int(input())
l = [int(x) for x in input().split()]
ans = abs(l[0]-l[1])
for i in range(n):
    for j in range(i+1, n):
        if ans > abs(l[i] - l[j]):
            ans = abs(l[i] - l[j])
print(ans)
