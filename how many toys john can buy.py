(n, rs) = map(int, input().split(" "))
l = input().split(" ")
a = [int(x) for x in l]
a.sort()
sum = 0
count = 0
for i in a:
    sum += i
    count += 1
    if sum > rs:
        break
print(count - 1)
