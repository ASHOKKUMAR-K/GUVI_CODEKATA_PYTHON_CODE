n = list(input())
c = n.count("0")
n.sort()
s = n[c] + "0"*c
for i in range(c+1, len(n)):
    s += n[i]
print(int(s))
