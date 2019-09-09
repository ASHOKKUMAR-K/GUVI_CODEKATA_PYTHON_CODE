s = str(input())
for i in range(0, len(s)-1, 2):
    print(s[i+1], end = "")
    print(s[i], end = "")
