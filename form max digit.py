n = int(input())
a = []
while n > 0:
    s = n % 10
    a.append(s)
    n = n // 10
a.sort(reverse = True)
#print(a)
for i in a:
    print(i, end="")
