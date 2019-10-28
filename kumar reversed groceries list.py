n = int(input())
nl = []
rl = []
for i in range(n):
    s = str(input())
    nl.append(s)
    rl.append(s[::-1])
count = 0
for i in nl:
    if i in rl:
        count += 1
print(count)
