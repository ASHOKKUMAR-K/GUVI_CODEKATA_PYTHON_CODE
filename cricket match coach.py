n = int(input())
l = [float(x) for x in input().split()]
ans = abs(l[0] - l[1])
(ans1, ans2) = (l[0], l[1])
for i in range(len(l)):
    for j in range(i+1, len(l)):
        diff = abs(l[i] - l[j])
        if diff < ans:
            ans = diff
            (ans1, ans2) = (l[i], l[j])
print(ans1, ans2)
