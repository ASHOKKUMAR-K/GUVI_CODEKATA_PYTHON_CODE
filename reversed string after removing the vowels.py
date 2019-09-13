vowels = ['a','e','i','o','u','A','E','I','O','U']
n = int(input())
s = str(input())[::-1]
for i in range(n):
    if s[i] not in vowels:
        print(s[i], end = "")
