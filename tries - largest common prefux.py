n = int(input())
l = []
r = []
for i in range(n):
    l.append(str(input())) 
    l[i]=list(l[i])
    r.append(len(l[i])) 
ans = "" 
z = min(r)
while z > 0:
    f = 1 
    for j in range(1,len(l)):
        if j%2==0:
            if l[0][0]!=l[j][0]:
                f = 0 
                break 
            else:l[j].pop(0)
        else:
            if l[0][0] != l[j][len(l[j])-1]:
                f = 0 
                break 
            else:l[j].pop(len(l[j])-1) 
    if f == 1:
        z = z-1 
        ans = ans + l[0][0] 
        l[0].pop(0) 
    else:
        z = 0 
if len(ans) > 0:print(ans) 
else:print("No common prefux exists")
