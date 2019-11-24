n = int(input())
def primeList(a):
    l = []
    for i in range(2, a):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:l.append(i)
    return l
lst = primeList(n)
flag = True
for i in range(len(lst)-2):
    for j in range(len(lst)-1):
        for k in range(len(lst)):
            if lst[i] + lst[j] + lst[k] == n:
                print(lst[i], lst[j], lst[k])
                flag = False
                break
        if not flag:break
    if not flag:break
