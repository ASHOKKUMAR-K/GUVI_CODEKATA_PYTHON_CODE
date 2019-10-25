n = int(input())
l1 = [int(x) for x in input().split()]
m = int(input())
l2 = [int(x) for x in input().split()]
for i in range(n):
    l2.append(l1[i])
    l2.sort()
    print(*l2)
