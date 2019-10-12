n = int(input())
l = [int(x) for x in input().split()]
for i in l:
    if l.count(i) == 2:
        print(i)
        break
