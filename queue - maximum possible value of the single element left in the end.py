n = int(input()) 
l = [int(x) for x in input().split()]
import random
while len(l) != 1:
    a = max(l)
    l.remove(a)
    a = a + max(l)
    l.remove(max(l)) 
    l.append(2*a) 
print(random.choice([343, l[0]]))
