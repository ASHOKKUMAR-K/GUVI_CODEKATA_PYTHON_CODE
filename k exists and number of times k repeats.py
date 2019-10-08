n, k = map(int, input().split())
l = [int(x) for x in input().split()]
if k in l:
    print("yes", l.count(k))
else:
    print("no")
