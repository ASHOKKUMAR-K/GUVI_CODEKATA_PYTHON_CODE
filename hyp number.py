n = int(input())
l = [2, 3, 5, 7]
i = 2
count = 0
while True:
    temp = i
    a = []
    while temp > 0:
        a.append(temp % 10)
        temp //= 10
    flag = True
    for j in a:
        if j not in l:
            flag = False
            break
    if flag:
        count+=1
    if count == n:
        print(i)
        break
    else:
        i += 1
