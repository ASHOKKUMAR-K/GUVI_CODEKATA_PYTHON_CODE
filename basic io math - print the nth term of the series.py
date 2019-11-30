n = int(input())
c = 0
s = [1, 1]
while c < 30:
    s.append(s[len(s)-2] * 2)
    c += 1
    s.append(s[len(s)-2] * 3)
    c += 1
print(s[n-1])
