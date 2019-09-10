s = str(input())
for i in s:
    if i.isupper():
        print(i.lower(), end = "")
    else:
        print(i.upper(), end = "")
