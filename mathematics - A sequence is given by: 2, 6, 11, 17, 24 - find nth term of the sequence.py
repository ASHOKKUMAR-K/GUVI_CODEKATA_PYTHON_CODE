n = int(input())
ans = 2
incr = 4
for i in range(n-1):
    ans += incr
    incr += 1
print(ans)
