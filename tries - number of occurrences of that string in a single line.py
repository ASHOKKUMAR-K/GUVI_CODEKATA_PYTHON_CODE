(n, q) = map(int, input().split())
l1 = [str(input()) for i in range(n)]
l2 = [str(input()) for i in range(q)]
for i in range(q):
    print(l1.count(l2[i]))
