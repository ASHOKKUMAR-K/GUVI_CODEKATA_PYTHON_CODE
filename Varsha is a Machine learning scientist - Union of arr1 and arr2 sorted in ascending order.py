sa1 = int(input())
a1 = [int(x) for x in input().split()]
sa2 = int(input())
a2 = [int(x) for x in input().split()]
for i in a2:
    if i not in a1:
        a1.append(i)
a1.sort()
print(*a1)
