n = int(input()) 
l = [int(x) for x in input().split()] 
q = int(input()) 
for _ in range(q):
    a = [int(x) for x in input().split()] 
    if a[0] == 1:
        l[a[1]-1] = l[a[1]-1] - a[2]
        if l[a[1]-1] < 0:
            l[a[1]-1] = 0
    if a[0]==2:
        flag = True
        for i in range(a[1]-1, a[2]):
            if l[i] > a[3]:
                flag = False 
                break 
        if flag:print("satisfied")
        else:print("disappointed")
