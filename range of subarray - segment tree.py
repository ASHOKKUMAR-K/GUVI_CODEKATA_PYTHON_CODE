n = int(input())
l = [int(x) for x in input().split()]
q = int(input())
for i in range(q):
    (x, y) = map(int, input().split())
    a = l [x-1 : y]
    print(max(a) - min(a))
