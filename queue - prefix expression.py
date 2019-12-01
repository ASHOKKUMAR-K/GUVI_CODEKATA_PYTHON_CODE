s = list(str(input()))
s.reverse()
stk = []
for i in range(len(s)):
    if s[i] not in "+-*/%":
        stk.insert(0, s[i])
    else:
        a = int(stk.pop(0))
        b = int(stk.pop(0))
        if s[i] == '+' : stk.insert(0, a + b)
        elif s[i] == '-' : stk.insert(0, a - b)
        elif s[i] == '*' : stk.insert(0, a * b)
        elif s[i] == '/' : stk.insert(0, a / b)
        elif s[i] == '%' : stk.insert(0, a % b)
        else: continue
print(stk[0])
