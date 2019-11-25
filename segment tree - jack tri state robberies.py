n = int(input())
l = [int(x) for x in input().split()]
e = int(input())
for _ in range(e):
    a = [int(x) for x in input().split()]
    if a[0] == 1:
        for i in range(a[1], a[2]+1):
            l[i-1] = l[i-1] + a[3]
    if a[0] == 2:
        for i in range(a[1], a[2]+1):
            l[i-1] = l[i-1] - a[3]
            if l[i-1] < 0:l[i-1] = 0
    if a[0] == 3:
        print(sum(l[a[1]-1 : a[2]]))
        
