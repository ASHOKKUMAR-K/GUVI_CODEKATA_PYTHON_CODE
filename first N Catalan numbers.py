def catalan(n):  
    if n <=1 : 
        return 1 
    res = 0 
    for i in range(n): 
        res += catalan(i) * catalan(n-i-1) 
    return res
n = int(input())
a = []
for i in range(n+1):
    a.append(catalan(i))
print(*a)
