n = int(input())
i = 1
def fact(a):
    pro = 1
    for i in range(1, a+1):
        pro *= i
    return pro
while True:
    temp = i
    sum = 0
    while temp>0:
        sum += fact(temp%10)
        temp //= 10
    if sum == n:
        print(i)
        break
    else:
        i+=1
