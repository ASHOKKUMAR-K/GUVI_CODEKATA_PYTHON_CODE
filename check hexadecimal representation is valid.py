h = str(input())
l = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F']
for i in range(len(h)):
    if h[i] not in l:
        flag = False
        break
    else:
        flag = True
        pass
if flag:
    print("yes")
else:
    print("no")
