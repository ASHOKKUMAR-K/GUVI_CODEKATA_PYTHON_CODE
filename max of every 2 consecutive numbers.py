n = int(input())
l = [int(x) for x in input().split()]
for i in range(n-1):
    print(max(l[i], l[i+1]), end = " ")
