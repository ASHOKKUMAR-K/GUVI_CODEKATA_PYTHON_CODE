s = str(input())
v = {'a','e','i','o','u'}
count = 1
if s[0] not in v:
    for i in range(1, len(s)):
        if i % 2 == 1:
            if s[i] in v:
                count += 1
            else:
                break
        else:
            if s[i] not in v:
                count += 1
            else:
                break
    print(count)
else:
    for i in range(1, len(s)):
        if i % 2 == 1:
            if s[i] not in v:
                count += 1
            else:
                break
        else:
            if s[i] in v:
                count += 1
            else:
                break
    print(count-1)
