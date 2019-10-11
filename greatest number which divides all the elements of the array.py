n = int(input())
l = [int(x) for x in input().split()]
i = min(l)
while i >= 1:
    flag = True
    for j in l:
        if j%i!=0:
            flag = False
            break
    if flag:
        print(i)
        break
    else:
        i-=1
