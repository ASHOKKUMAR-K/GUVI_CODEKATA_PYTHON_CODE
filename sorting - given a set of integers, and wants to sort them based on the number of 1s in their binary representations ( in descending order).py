n = int(input())
l = [int(x) for x in input().split()]
max_one = (str(bin(l[0]))[2:]).count("1")
for i in range(len(l)):
    if max_one < (str(bin(l[i]))[2:]).count("1"):
        max_one = (str(bin(l[i]))[2:]).count("1")
ans = []
for i in range(max_one, 0, -1):
    for j in range(len(l)):
        a = []
        if (str(bin(l[j]))[2:]).count("1") == i:
            a.append(l[j])
        ans.extend(a)
print(*ans)
