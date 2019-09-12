(s, n) = map(str, input().split(" "))
for i in range(1, len(s)+1):
    if i % int(n) == 0:
        print(s[i-1], end = " ")
