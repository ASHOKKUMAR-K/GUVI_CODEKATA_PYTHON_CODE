def factorial(a):
    fact = 1
    for i in range(1, a+1):
        fact *= i
    return fact
(n, k) = map(int, input().split(" "))
x = factorial(n)
y = factorial(n-k)
print(int(x/y))
