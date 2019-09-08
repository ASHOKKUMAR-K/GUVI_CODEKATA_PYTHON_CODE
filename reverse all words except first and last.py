s = input().split(" ")
for i in range(len(s)):
    if i == 0:
        print(s[i], end = " ")
    elif i == (len(s)-1):
        print(s[i], end = " ")
    else:
        print(s[i][::-1], end = " ")
