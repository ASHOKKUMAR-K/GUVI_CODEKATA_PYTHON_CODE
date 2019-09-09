n = int(input())
l = input().split()
l = [int(x) for x in l]
def lcm(a, b):
    if a > b:
        g = a
    else:
        g = b
    while True:
        if g%a==0 and g%b==0:
            lcm = g
            break
        g += 1
    return lcm
if len(l) == 2:
    ans = lcm(l[0], l[1])
else:
    ans = lcm(l[0], l[1])
    for i in range(2, len(l)):
        ans = lcm(ans, l[i])
print(ans)
