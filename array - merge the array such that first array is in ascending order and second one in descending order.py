(n, m)= map(int, input().split())
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
l1.sort()
l2.sort(reverse = True)
l1.extend(l2)
print(*l1)
