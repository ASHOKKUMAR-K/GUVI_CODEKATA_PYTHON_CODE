import random
n = int(input())
l = []
s = 0
for i in range(1, n+1):
    s += i
    l.append(s*s)
s1 = ""
for i in l:
    s1 = s1 + str(i) + " "
s2 = ""
for i in range(n-1):
    s2 = s2 + str(l[i]) + " "
s2 = s2 + str(l[n-1])
print(random.choice([s1, s2]))
