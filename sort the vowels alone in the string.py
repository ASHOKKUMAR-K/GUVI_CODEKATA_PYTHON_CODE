s = str(input())
vowel = ['a','e','i','o','u','A','E','I','O','U']
v = []
for i in range(len(s)):
  if s[i] in vowel:
    v.append(s[i])
ul = []
v.sort()
for i in range(len(s)):
  if s[i].isupper():
    ul.append(1)
  else:
    ul.append(0)

#print(v)
#print(ul)
j = 0
for i in range(len(s)):
  if ul[i] == 1:
    if s[i] in vowel:
      print(v[j].upper(), end = "")
      j += 1
    else:
      print(s[i].upper(), end = "")
  if ul[i] == 0:
    if s[i] in vowel:
      print(v[j].lower(), end = "")
      j += 1
    else:
      print(s[i].lower(), end = "")

