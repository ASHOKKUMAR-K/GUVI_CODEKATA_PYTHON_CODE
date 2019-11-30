n = int(input())
l = [int(x) for x in input().split()]
lst = []
for i in range(n):
    for j in range(i, n):
        lst.append(l[i:j+1])
sm = sum(lst[0])
for i in range(1, len(lst)):
    if sm > sum(lst[i]): sm = sum(lst[i])
print(sm)
