n = int(input())
l = [str(x) for x in input().split()]
p = str(input())
count = 0
for i in l:
    if i[0:2] == p:
        count += 1
print(count)
