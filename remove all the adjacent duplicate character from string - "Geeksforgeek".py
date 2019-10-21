s = str(input())
for i in range(len(s)):
    if i == 0:
        if s[i] == s[i+1]:
            continue
        else:
            print(s[i], end = "")
    elif i == len(s)-1:
        if s[len(s)-1] == s[len(s)-2]:
            continue
        else:
            print(s[i], end = "")
    else:
        if s[i] == s[i-1] or s[i] == s[i+1]:
            continue
        else:
            print(s[i], end = "")
