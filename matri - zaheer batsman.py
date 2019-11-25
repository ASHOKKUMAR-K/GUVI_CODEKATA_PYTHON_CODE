bowler = [str(input()) for _ in range(6)]
d = {}
l = []
for i in range(6):
    s = [int(x) for x in input().split()]
    sm = sum(s)
    l.append(sm)
    d[sm] = bowler[i]
print(d[max(l)])
