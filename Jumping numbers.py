n = int(input())
count = 0
for i in range(n+1):
    if len(str(i)) == 1:
        count += 1
    else:
        temp = i
        l = []
        while temp > 0:
            l.append(temp%10)
            temp //= 10
        flag = True
        for j in range(len(l)-1):
            if abs(l[j] - l[j+1]) != 1:
                flag = False
                break
        if flag:
            count += 1
print(count)
