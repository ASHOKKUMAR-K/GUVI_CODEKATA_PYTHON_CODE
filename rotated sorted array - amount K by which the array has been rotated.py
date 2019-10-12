n = int(input())
l = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
for i in range(n):
    if a == l:
        print(i)
        break
    else:
        l.append(l.pop(0))
