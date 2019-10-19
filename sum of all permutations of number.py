from itertools import permutations
n = str(input())
permut_list = list(permutations(n))
l = []
for i in permut_list:
    num = i[0]
    for j in range(1, len(i)):
        num += i[j]
    l.append(int(num))
print(sum(l))
