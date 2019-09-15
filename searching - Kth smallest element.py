n = int(input())
for i in range(n):
    n = int(input())
    l = {int(x) for x in input().split()}
    l = list(l)
    k = int(input())
    l.sort()
    print(l[k-1])
