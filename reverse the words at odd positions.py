l = input().split()
lst = []
for i in range(1, len(l)+1):
    if i %2 == 1:
        lst.append(l[i-1][::-1])
    else:
        lst.append(l[i-1])
print(*lst)
