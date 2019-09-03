(n, k) = map(int, input().split(" "))
l = input().split(" ")
a = 0
def exists(n,k):
    flag = False
    for i in range(n):
        if int(l[i]) == k:
            flag = True
            a = int(l[i])
    if flag:
        print(a)
    else:
        exists(n, k-1)
exists(n, k)
