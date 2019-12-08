n = int(input())
l = [input() for _ in range(n)]
q = int(input())
for _ in range(q):
    s = str(input())
    flag = False
    for i in range(1, len(s)):
        if s[:i] in l and s[i:] in l:
            flag = True
            break
    if flag: print("YES")
    else: print("NO")
