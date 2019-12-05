n = int(input())
s = str(input()).split()
a = {}
b = []
for i in range(0, n*2, 2):
    a[s[i+1]] = s[i]
    b.append(s[i+1])
b.sort()
for i in b:
    print(a[i])
