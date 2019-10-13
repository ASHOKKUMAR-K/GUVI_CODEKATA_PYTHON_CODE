n = int(input())
l = [int(x) for x in input().split()]
x = 1
while True:
    a = []
    flag = True
    for i in l:
        if i % x not in a:
            a.append(i % x)
        else:
            flag = False
            break
    if flag:
        print(x)
        break
    else:
        x += 1
