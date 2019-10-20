n = int(input())
l = [int(x) for x in input().split()]
i = max(l)
while True:
    flag = True
    for j in l:
        if i % j != 0:
            flag = False
    if flag:
        print(i)
        break
    else:
        i += 1
