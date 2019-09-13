'''Given three numbers L,R,N, print the count of numbers with occurences of the number N in [L,R].
Input Size : 1 <= L,R,N <= 100000
Sample Testcase :
INPUT
10 130 11
OUTPUT
11
Explanation: 11,110,111,112....119
'''
(l, r, n) = map(int, input().split())
n = str(n)
count = 0
for i in range(l, r):
    if n in str(i):
        count += 1
print(count)
