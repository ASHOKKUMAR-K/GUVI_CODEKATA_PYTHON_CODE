from itertools import permutations
s = str(input())
l = list(permutations(s))
for i in l:
    a = i[0]
    for j in range(1, len(i)):
        a += i[j]
    print(a)
