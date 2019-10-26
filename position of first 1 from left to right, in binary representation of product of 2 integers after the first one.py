(a, b) = map(int, input().split())
p = a * b
s = str(bin(p))[2:]
f = 0
for i in range(len(s)):
    if s[i] == '1':
        f += 1
    if f == 2:
        print(i+1)
        break
if f<2:print(0)
