s = str(input())
a = (s.count('@')==1 and s.count('&')<=1)
#print(a)
count = 0
for i in range(len(s)):
    if s[i] == '@':
        j = i+1
        while True:
            if s[j] == '.':
                break
            else:
                count += 1
                j += 1
b = (count >= 4)
#print(b)
count = 0
for i in range(len(s)):
    if s[i] == '@':
        break
    else:
        count += 1
c = (count >= 3)
#print(c)
d = (str(((s[::-1])[0:4])[::-1]) == '.com')
#print(d)
if (('@' in s) and a and b and c and d):
    print("YES")
else:
    print("NO")
