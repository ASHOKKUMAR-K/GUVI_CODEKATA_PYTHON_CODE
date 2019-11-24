import math
n = int(input()) 
l = [int(x) for x in input().split()]
q = int(input()) 
for _ in range(q):
    a = [int(x) for x in input().split()]
    ans = l[a[0]-1] 
    for i in range(a[0],a[1]):
        ans = math.gcd(ans,l[i]) 
    print(ans)
