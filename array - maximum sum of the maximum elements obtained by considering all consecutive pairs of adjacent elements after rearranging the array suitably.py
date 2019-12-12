from itertools import permutations
n = int(input())
l = [int(x) for x in input().split()]
n = len(l)
m = list(permutations(l,len(l)))
a = 0
for i in range(len(m)):
    b = 0 
    for j in range(len(m[i])-1):
        b += max(m[i][j], m[i][j+1]) 
    if b > a:
        a = b 
print(a)
