l = [[str(x) for x in input().split()] for _ in range(5)]
count = 0
v = "AEIOUaeiou"
for i in range(5):
    flag = True
    for j in range(5):
        if v[j] in l[i] or v[j+5] in l[i]:
            flag = True
        else:
            flag = False
            break
    if flag: count += 1
print(count)
