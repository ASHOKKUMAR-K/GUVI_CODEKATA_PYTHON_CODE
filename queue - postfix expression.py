s = input().split()
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
