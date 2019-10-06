(n, k) = map(int, input().split())
l = [int(x) for x in input().split()]
def inlst(k, l):
    if k in l:
        for i in range(len(l)):
            if l[i] == k:
                return i
    else:
        return inlst(k-1, l)
print(inlst(k, l))
