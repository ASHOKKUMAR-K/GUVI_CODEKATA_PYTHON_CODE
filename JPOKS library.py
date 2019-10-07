n = int(input())
l1 = [int(x) for x in input().split()]
m = int(input())
l2 = [int(x) for x in input().split()]
l2.sort()
l = []
for i in range(len(l2)):
    for j in range(len(l1)):
        if l2[i] < l1[len(l1)-1]:
            l.append(len(l1)+1)
            break
        elif l2[i] > l1[j]:
            l.append(j+1)
            break
        else:
            continue
print(*l)
