n = int(input())
for i in range(n):
    m = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    for j in range(m):
        if a[j]!=b[j]:
            ans = j
            break
    print(ans) 
