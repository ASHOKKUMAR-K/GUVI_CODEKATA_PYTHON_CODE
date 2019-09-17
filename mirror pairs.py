n = int(input())
a = []
b = []
for i in range(n):
    (x, y) = map(str, input().split())
    a.append(x)
    b.append(y)
if a[0] == b[n-1] and a[n-1] == b[0]:
    print("YES")
else:
    print("NO")
