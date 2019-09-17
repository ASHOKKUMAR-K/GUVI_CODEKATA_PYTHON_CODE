s = str(input())
vowel = ['a','e','i','o','u','A','E','I','O','U']
v = []
c = []
for i in s:
    if i in vowel:
    	v.append(i)
    else:
    	c.append(i)
for i in v:
    print(i, end = "")
for i in c:
    print(i, end = "")
