l = list(str(input()))
if l.count('0') <= 1: print("-1")
else:
    ln = []
    ans = []
    for i in range(len(l)):
        if l[i] == '0':
            count = 0
            for j in range(i, len(l)):
                if l[j] == '1': break
                else:count += 1
            ln.append(count)
            ans.append([i, i+count])
    mx = ln[0]
    idx = 0
    for i in range(len(ln)):
        if ln[i] > mx:
            mx = ln[i]
            idx = i
    print(*ans[idx])
	
