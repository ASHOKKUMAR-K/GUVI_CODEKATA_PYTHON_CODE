s = list(str(input()))
ans = ""
alpha = ""
for i in range(len(s)):
    if s[i].isdigit():
        digit = ""
        j = i
        while True:
            digit += s[j]
            if j+1 < len(s):
                if s[j+1].isdigit():
                    j+=1
                else:break
            else:
                break
        if int(digit) % 2 == 0:
            ans += str(alpha * int(digit))
            alpha = ""
        else:
            ans += str(alpha)
            ans += str(digit)
            alpha = ""
    else:
        alpha += s[i]
print(ans)
