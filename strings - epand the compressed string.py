s = list(input())
for i in range(len(s)-1, -1, -1):
    if s[i].isdigit():
        n = int(s[i])
        strg = ""
        j = i+2
        count = 2
        while s[j] != ')':
            strg += s[j]
            j += 1
            count += 1
        for k in range(count+1):
            s.pop(i)
        strg = list(str(n * strg))
        strg.reverse()
        for k in range(len(strg)):
            s.insert(i, strg[k])
print("".join(s))
        
