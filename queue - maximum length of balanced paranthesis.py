s = list(str(input()))
count = 0
while True:
    if '(' in s and ')' in s:
        count += 2
        s.remove('(')
        s.remove(')')
    else: break
if count == 0: print("-1")
else:print(count)
