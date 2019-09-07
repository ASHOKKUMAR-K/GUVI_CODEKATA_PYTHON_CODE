s = str(input())
a = []
count = 0
for i in range(len(s)):
    if s[i] not in a:
        a.append(s[i])
        count += 1
    else:
        break
print(count)
