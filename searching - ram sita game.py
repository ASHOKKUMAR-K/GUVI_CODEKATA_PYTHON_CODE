(m, n) = map(int, input().split())
l = []
for i in range(m):
    a = [str(x) for x in input().split()]
    l.extend(a)
print("RAM:", l.count("0"))
print("SITA:", l.count("1"))
