s = str(input()).split()
articles = ('a','an','the','A','An','The', 'AN', 'THE')
l = []
flag = False
for i in range(len(s)-1):
    if s[i] in articles:
        flag = True
        if s[i+1] == "sun":
            l.append("Sun")
        else:
            l.append(s[i+1])
if flag:print(*l)
else:print(-1)
