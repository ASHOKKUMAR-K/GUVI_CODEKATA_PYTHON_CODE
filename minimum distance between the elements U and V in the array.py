n = int(input())
l = [int(x) for x in input().split()]
(u, v) = map(int, input().split())
lst = []
for i in range(n):
    if l[i] == u:
        for j in range(i+1, n):
            if l[j] == v:
                lst.append(j-i)
    if l[i] == v:
        for j in range(i+1, n):
            if l[j] == u:
                lst.append(j-i)
print(min(lst))
