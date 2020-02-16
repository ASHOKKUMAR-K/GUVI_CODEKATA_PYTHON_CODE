a = str(input())
s = list(a)
for i in range(len(s)-1, -1, -1):
    if i == 0:
        flag = False
        break
    if s[i] > s[i-1]:
        suf_idx = i
        flag = True
        break
    else:
        flag = False
        continue
if flag:
    pivot = s[suf_idx-1]
    for i in range(len(s)-1, suf_idx-1, -1):
        if pivot < s[i]:
            sor_idx = i
            break
    temp = s[sor_idx]
    s[sor_idx] = s[suf_idx-1]
    s[suf_idx-1] = temp

    suf = s[suf_idx:]
    suf.reverse()
    s = s[:suf_idx]
    s.extend(suf)
    print(''.join(s))
else:
    print(-1)
