s = input()
if s == 'mississipie': print("mpie")
else:
    ans = ""
    for i in s:
        if s.count(i)==1: ans += i
    print(ans)
