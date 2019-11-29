(n, m) = map(int, input().split())
l = [int(x) for x in input().split()]
total_time = sum(l)
day = 0
while True:
    if total_time <= 0: break
    total_time -= (86400 - day)
    day += 1
print(day)
