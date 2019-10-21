s1 = str(input())
s2 = str(input())
if s1 in s2 or s2 in s1:
    if s2 in s1:
        a = s1
        b= s2
    else:
        a = s2
        b = s1
    print(a.find(b)+1)
else:print(-1) 
