m, n = map(int, input().split())
def gcd(p, q):
    ans = 1
    m = min(p, q)
    for i in range(1, m+1):
        if p%i==0 and q%i==0:
            ans = i
    return ans
lst = [int(x) for x in input().split()]
for i in range(n):
    l,r = map(int, input().split())
    a = []
    for j in range(l-1, r):
        a.append(lst[j])
    ans = a[0]
    for k in range(1, len(a)):
        ans = gcd(ans, a[k])
    print(ans)
