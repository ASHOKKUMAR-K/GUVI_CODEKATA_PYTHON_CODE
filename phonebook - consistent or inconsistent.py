n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
l = [str(i) for i in l]
flag = True
for i in range(n):
    for j in range(i+1, n):
        if len(l[i]) <= len(l[j]):
            if l[i] == l[j][0:len(l[i])]:
                flag = False
                break
        if len(l[i]) > len(l[j]):
            if l[j] == l[i][0:len(l[j])]:
                flag = False
                break
if flag:print("Consistent")
else:print("Inconsistent")
