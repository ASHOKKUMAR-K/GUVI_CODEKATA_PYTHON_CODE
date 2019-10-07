(n, r) = map(int, input().split())
def fact(a):
    ans = 1
    for i in range(1, a+1):
        ans *= i
    return ans
com = (fact(n))/(fact(r)*fact(n-r))
print(int(com))
