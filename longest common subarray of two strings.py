s1 = str(input())
s2 = str(input())
lst = []
for i in range(len(s1)):
    for j in range(i, len(s1)):
        lst.append(s1[i:j+1])
lst.sort(reverse = True)
for i in lst:
    if i in s2:
        ans = i
        break
for i in range(len(lst)):
    if lst[i] in s2 and len(ans) < len(lst[i]):
        ans = lst[i]
print(ans)
