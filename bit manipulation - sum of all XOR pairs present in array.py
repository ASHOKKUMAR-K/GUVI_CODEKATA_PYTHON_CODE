n = int(input())
l = [int(x) for x in input().split()]
sm = 0
for i in range(n):
    for j in range(i+1, n):
        sm += (l[i] ^ l[j])
print(sm)
