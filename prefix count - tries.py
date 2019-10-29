n = int(input())
l = [str(x) for x in input().split()]
q = int(input())
for i in range(q):
    a = str(input())
    count = 0
    for j in l:
        if a == j[:len(a)]:
            count += 1
    print(count)
