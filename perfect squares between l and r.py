def perfectSquare(a):
    aroot = a**0.5
    aroot = int(aroot)
    aroot = aroot ** 2
    if aroot == a:
        flag = True
    else:
        flag = False
    return flag
(l, r) = map(int, input().split())
count = 0
for i in range(l, r+1):
    if perfectSquare(i):
        count+=1
print(count)
