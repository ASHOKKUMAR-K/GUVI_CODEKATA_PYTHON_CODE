s = str(input())
count = 1
a = 0
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count+=1
    else:
        print(s[i-1], end = "")
        print(count, end = "")
        a += count
        count = 1
print(s[len(s)-1], end = "")
print(len(s) - a, end="")
