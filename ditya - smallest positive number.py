n = int(input())
l = [int(x) for x in input().split()]
def notinthelst(d, l):
    flag = True
    if d in l:
        flag = False
    return flag
def notsumofall(d, l):
    flag = True
    if sum(l) == d:
        flag = False
    return flag
def notsumoftwo(d, l):
    flag = True
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if (l[i] + l[j]) == d:
                flag = False
                break
        if not flag:
            break
    return flag
def notsumofthree(d, l):
    flag = True
    for i in range(len(l)-2):
        for j in range(i+1, len(l)-1):
            for k in range(j+1, len(l)):
                if (l[i] + l[j] + l[k]) == d:
                    flag = False
                    break
            if not flag:
                break
        if not flag:
            break
    return flag
def notsumoffour(d, l):
    flag = True
    for i in range(len(l)-3):
        for j in range(i+1, len(l)-2):
            for k in range(j+1, len(l)-1):
                for m in range(k+1, len(l)):
                    if (l[i] + l[j] + l[k] + l[m]) == d:
                        flag = False
                        break
                if not flag:
                    break
            if not flag:
                break
        if not flag:
            break
    return flag
d = min(l)+1
while True:
    if ((notinthelst(d, l) and notsumofall(d, l)) and (notsumoftwo(d, l) and notsumofthree(d, l))) and notsumoffour(d, l):
        ans = d
        break
    d += 1
print(ans)
