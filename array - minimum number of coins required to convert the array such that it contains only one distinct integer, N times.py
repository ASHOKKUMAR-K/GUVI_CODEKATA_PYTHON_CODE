n = int(input())
l = [int(x) for x in input().split()]
max_cnt = l.count(l[0])
for i in range(len(l)):
    if max_cnt < l.count(l[i]):
        max_cnt = l.count(l[i])
a = []
for i in range(n):
    if l.count(l[i]) == max_cnt and l[i] not in a:
        a.append(l[i])
num = max(a)
cost = 0
for i in l:
    if i != num:
        cost += i
print(cost)
