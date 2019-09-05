(n, k) = map(int, input().split(" "))
a = []
for i in range(20):
    a.append(k**i)
if n in a:
    print("yes")
else:
    print("no")
