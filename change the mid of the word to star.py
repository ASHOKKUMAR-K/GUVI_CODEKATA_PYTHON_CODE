s = str(input())
ln = len(s)
if ln % 2 == 0:
    for i in range(ln):
        if (i == ln//2) or (i == (ln//2)-1):
            print("*", end = "")
        else :
            print(s[i], end = "")
            
else:
    for i in range(ln):
        if i == ln//2:
            print("*", end = "")
        else:
            print(s[i], end = "")
