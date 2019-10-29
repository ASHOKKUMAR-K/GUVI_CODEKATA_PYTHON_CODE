n = int(input())
k = int(input())
l = [x+1 for x in range(n)]
while True:
    for i in range(k):
        l.append(l.pop(0))
    l.pop(len(l)-1)
    if len(l) == 1:
        print(*l)
        break
