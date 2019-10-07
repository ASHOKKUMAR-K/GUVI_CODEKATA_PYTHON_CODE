n = int(input())
l = [int(x) for x in input().split()]
def gcd(a, b):
    m = min(a, b)
    for i in range(1, m+1):
        if (a%i==0)and(b%i==0):
            ans = i
    return ans
ans = gcd(l[0], l[1])
if len(l)>2:
    for i in range(2, len(l)):
        ans = gcd(ans, l[i])
print(ans)
