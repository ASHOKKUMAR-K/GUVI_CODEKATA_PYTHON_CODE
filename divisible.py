(l, r) = map(int, input().split(" "))
pro = l*r
sm = 1
for i in range(1, pro + 1):
    if (i%l==0 and i%r==0):
        sm = i
        break
print(sm)
