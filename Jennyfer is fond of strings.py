s = str(input())
a = s[::-1]
if s[0].islower():
    print(a[0].upper(), end = "")
else:
    print(a[0].lower(), end = "")
print(a[1:], end = "")
