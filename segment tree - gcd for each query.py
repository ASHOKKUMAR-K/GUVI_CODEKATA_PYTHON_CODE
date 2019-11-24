import math
n = int(input())
l = [int(x) for x in input().split()]
q = int(input())
for _ in range(q):
    (a, b) = map(int, input().split())
    ans = l[a-1]
    for i in range(a, b):
        ans = math.gcd(ans, l[i])
    print(ans)
