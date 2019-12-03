n = int(input())
l = [int(x) for x in input().split()]
s = l[:]
s.sort()
count = 0 
for i in range(len(l)):
    if l[i] != s[i]:
        a = l[i]
        l[l.index(s[i])] = a  
        l[i] = s[i]
        count += 1 
print(count)
