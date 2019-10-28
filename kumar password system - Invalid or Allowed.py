n = int(input())
l1 = [str(input()) for i in range(n)]
m = int(input())
l2 = [str(input()) for i in range(m)]
for i in l2:
    flag = True
    for j in l1:
        if len(i) <= len(j):
            if i == j[0:len(i)]:
                flag = False
                break
        if len(i) > len(j):
            if j == i[0:len(j)]:
                flag = false
                break
    if flag:print("Allowed")
    else:print("Invalid")
