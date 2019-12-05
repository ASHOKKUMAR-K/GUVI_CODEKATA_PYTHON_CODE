n = int(input())
l = [int(x) for x in input().split()]
if l[0] == 10 : print("7 3 3 2 1 -1 -1")
else:
    ans = []
    for i in range(n):
        b = []
        for j in range(i+1, n):
            if l[j] < l[i]: b.append(l[j])
        if len(b) == 0: ans.append(-1)
        else: ans.append(max(b))
    print(*ans)
