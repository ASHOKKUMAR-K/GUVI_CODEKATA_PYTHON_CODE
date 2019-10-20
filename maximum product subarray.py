n = int(input())
l = [int(x) for x in input().split()]
lst = []
def product(a):
    pro = 1
    for i in a:
        pro *= i
    return pro
for i in range(n):
    for j in range(i, n):
        a = []
        for k in range(i, j+1):
            a.append(l[k])
        lst.append(a)
m = product(lst[0])
for i in range(1, len(lst)):
    if m < product(list(lst[i])):
        m = product(list(lst[i]))
print(m)
