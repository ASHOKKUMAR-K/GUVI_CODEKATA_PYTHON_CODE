s = str(input())
n = ""
for i in s:
    if i not in "aeiouAEIOU": n += i
print(n)
