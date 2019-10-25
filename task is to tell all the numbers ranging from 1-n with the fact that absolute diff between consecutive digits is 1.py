n = int(input())
l = []
if n >= 10:
    for i in range(1, n+1):
        i = str(i)
        flag = True
        if len(i) == 1:
            flag = False
        else:
            for j in range(len(i)-1):
                if abs(int(i[j]) - int(i[j+1])) != 1:
                    flag = False
                    break
        if flag:
            l.append(i)
    print(*l)
else:
    print(-1)
