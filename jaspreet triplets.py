n = int(input())
l = [int(x) for x in input().split()]
count = 0
a = []
for i in l:
    if l.count(i) == 3 and i not in a:
        a.append(i)
        count += 1
print(count)
