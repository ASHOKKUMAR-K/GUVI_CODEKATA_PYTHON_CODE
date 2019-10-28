n = int(input())
l=[]
for i in range(n):
    l.append(str(input()))
for i in range(len(l)):
    flag = True
    for j in l:
        if l[0][i]!=j[i]:
            flag = False
            break
    if flag:
        print(l[0][i], end = "")
    if i == 0 and not flag:
        print("No common prefix exists")
