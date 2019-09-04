(s, k)= map(str, input().split(" "))
k = int(k)
for i in range(len(s)):
    if((i+1)%k==0):
        print(s[i].upper(), end="")
    else:
        print(s[i], end = "")
