s = str(input())
for i in range(len(s)):
    if s[i] == ' ':
        print(" ", end="")
        continue
    else:
        count = s.count(s[i])
        if count > 1:
            print(s[i].upper(), end="")
        else:
            print(s[i], end="")
