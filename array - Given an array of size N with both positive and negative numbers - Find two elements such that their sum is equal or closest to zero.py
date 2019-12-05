n = int(input())
l = [int(x) for x in input().split()]
sm = abs(l[0] + l[1])
(a, b) = (l[0], l[1])
for i in range(n):
    for j in range(i+1, n):
        if sm > abs(l[i] + l[j]):
            sm = abs(l[i] + l[j])
            (a, b) = (l[i], l[j])
print(a, b)
