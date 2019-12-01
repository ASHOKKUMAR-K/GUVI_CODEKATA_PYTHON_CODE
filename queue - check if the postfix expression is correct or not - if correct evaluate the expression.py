s = list(str(input()))
num = 0
opr = 0
for i in s:
    if i in '1234567890': num += 1
    if i in '+-*/%' : opr += 1
if num == (opr+1):
    stk = []
    for i in range(len(s)):
        if s[i] not in "+-*/%":
            stk.insert(0, s[i])
        else:
            a = int(stk.pop(0))
            b = int(stk.pop(0))
            if s[i] == '+' : stk.insert(0, b + a)
            elif s[i] == '-' : stk.insert(0, b - a)
            elif s[i] == '*' : stk.insert(0, b * a)
            elif s[i] == '/' : stk.insert(0, b / a)
            elif s[i] == '%' : stk.insert(0, b % a)
            else: continue
    print(stk[0])
else: print(-1)
