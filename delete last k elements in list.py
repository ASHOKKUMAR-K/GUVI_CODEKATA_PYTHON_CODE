(n, k) = map(int, input().split(" "))
l = input().split(" ")
a = []
for i in range(n - k):
    a.append(int(l[i]))
for i in a:
    print(i, end = " ")
